import torch
from collections import OrderedDict

from basicsr.archs import build_network
from basicsr.losses import build_loss
from basicsr.utils import get_root_logger
from basicsr.utils.registry import MODEL_REGISTRY
from .sr_model import SRModel

@MODEL_REGISTRY.register()
class WAEGANModel(SRModel):

    def init_training_settings(self):

        '''opt'''
        train_opt = self.opt['train']

        '''ema_decay in generator'''
        self.ema_decay = train_opt.get('ema_decay',0)
        if self.ema_decay > 0:
            logger = get_root_logger()
            logger.info(f'Use Exponential Moving Average with decay: {self.ema_decay}')
            # define network net_g with Exponential Moving Average (EMA)
            # net_g_ema is used only for testing on one GPU and saving
            # There is no need to wrap with DistributedDataParallel
            self.net_g_ema = build_network(self.opt['network_g']).to(self.device)
            # load pretrained model
            load_path = self.opt['path'].get('pretrain_network_g', None)
            if load_path is not None:
                self.load_network(self.net_g_ema, load_path, self.opt['path'].get('strict_load_g', True), 'params_ema')
            else:
                self.model_ema(0)  # copy net_g weight
            self.net_g_ema.eval()

        '''define d1'''
        self.net_d1 = build_network(self.opt['network_d1'])
        self.net_d1 = self.model_to_device(self.net_d1)
        self.print_network(self.net_d1)

        '''define d2'''
        self.net_d2 = build_network(self.opt['network_d2'])
        self.net_d2 = self.model_to_device(self.net_d2)
        self.print_network(self.net_d2)

        self.net_g.train()
        self.net_d1.train()
        self.net_d2.train()

        '''define losses'''

        if train_opt.get('pixel_opt'):
            self.cri_pix = build_loss(train_opt['pixel_opt']).to(self.device)
        else:
            self.cri_pix = None

        if train_opt.get('perceptual_opt') is not None:
            self.cri_perceptual = build_loss(train_opt['perceptual_opt']).to(self.device)
        else:
            self.cri_perceptual = None

        if train_opt.get('gan_opt'):
            self.cri_gan = build_loss(train_opt['gan_opt']).to(self.device)
        else:
            self.cri_gan = None

        if train_opt.get('ganall_opt'):
            self.cri_ganall = build_loss(train_opt['ganall_opt']).to(self.device)
        else:
            self.cri_ganall = None

        self.net_d_iters = train_opt.get('net_d_iters',1)
        self.net_d_init_iters = train_opt.get('net_d_init_iters',0)

        '''optimizers and schedulers'''

        self.setup_optimizers()
        self.setup_schedulers()

    def setup_optimizers(self):
        train_opt = self.opt['train']
        '''optimize g'''
        optim_type = train_opt['optim_g'].pop('type')
        self.optimizer_g = self.get_optimizer(optim_type, self.net_g.parameters(), **train_opt['optim_g'])
        self.optimizers.append(self.optimizer_g)
        # optimizer d1
        optim_type = train_opt['optim_d1'].pop('type')
        self.optimizer_d1 = self.get_optimizer(optim_type, self.net_d1.parameters(), **train_opt['optim_d1'])
        self.optimizers.append(self.optimizer_d1)
        # optimizer d2
        optim_type = train_opt['optim_d2'].pop('type')
        self.optimizer_d2 = self.get_optimizer(optim_type, self.net_d2.parameters(), **train_opt['optim_d2'])
        self.optimizers.append(self.optimizer_d2)

    def optimize_parameters(self, current_iter):

        '''
        TODO: modify arch to get 0.op 1.latent 2.mean 3.var
        try 0 and 1 to get result
        '''

        '''optimize net_g'''
        for p in self.net_d1.parameters():
            p.requires_grad = False
        for p in self.net_d2.parameters():
            p.requires_grad = False

        self.optimizer_g.zero_grad()
        # self.output, self.latent, self.mean, self.var = self.net_g(self.lq)
        self.output, self.latent = self.net_g(self.lq)

        l_g_total = 0
        loss_dict = OrderedDict()
        if (current_iter % self.net_d_iters == 0 and current_iter > self.net_d_init_iters):
            if self.cri_pix is not None:
                l_g_pix = self.cri_pix(self.output,self.gt)
                l_g_total += l_g_pix
                loss_dict['l_g_pix'] = l_g_pix
            if self.cri_perceptual is not None:
                l_g_percep, l_g_style = self.cri_perceptual(self.output,self.gt)
                if l_g_percep is not None:
                    l_g_total += l_g_percep
                    loss_dict['l_g_percep'] = l_g_percep
                if l_g_style is not None:
                    l_g_total += l_g_style
                    loss_dict['l_g_style'] = l_g_style
            '''
            TODO:
            Rewrite GAN LOSS
            '''
            fake_g_pred = self.net_d2(self.output)
            l_g_gan = self.cri_gan(fake_g_pred, True, is_disc = False)
            l_g_total += l_g_gan
            loss_dict['l_g_gan'] = l_g_gan


            l_g_total.backward()
            self.optimizer_g.step()

        '''optimize net_d'''
        for p in self.net_d1.parameters():
            p.requires_grad = True
        for p in self.net_d2.parameters():
            p.requires_grad = True
        self.optimizer_d1.zero_grad()
        self.optimizer_d2.zero_grad()
        #real
        #real_d = torch.randn_like(self.latent.detach()) * self.var.detach() + self.mean.detach()
        real_d = torch.randn_like(self.latent.detach())
        real_d_pred = self.net_d1(real_d)
        l_d_real = self.cri_gan(real_d_pred, True, is_disc = True)
        loss_dict['l_d_real'] = l_d_real
        loss_dict['out_d_real'] = torch.mean(real_d_pred.detach())
        l_d_real.backward()
        #fake
        fake_d = self.latent.detach().clone()
        fake_d_pred = self.net_d1(fake_d)
        l_d_fake = self.cri_gan(fake_d_pred, False, is_disc = True)
        loss_dict['l_d_fake'] = l_d_fake
        loss_dict['out_d_fake'] = torch.mean(fake_d_pred.detach())
        l_d_fake.backward()

        self.optimizer_d1.step()

        real_d2 = self.gt
        real_d2_pred = self.net_d2(real_d2)
        l_d_real_img = self.cri_ganall(real_d2_pred, True, is_disc = True)
        loss_dict['l_d_real_img'] = l_d_real_img
        loss_dict['out_d_real_img'] = torch.mean(real_d2_pred.detach())
        l_d_real_img.backward()

        fake_d2 = self.output.detach()
        fake_d2_pred = self.net_d2(fake_d2)
        l_d_fake_img = self.cri_ganall(fake_d2_pred, False, is_disc = True)
        loss_dict['l_d_fake_img'] = l_d_fake_img
        loss_dict['out_d_fake_img'] = torch.mean(fake_d2_pred.detach())
        l_d_fake_img.backward()

        self.optimizer_d2.step()

        self.log_dict = self.reduce_loss_dict(loss_dict)

        if self.ema_decay > 0:
            self.model_ema(decay=self.ema_decay)

    def save(self, epoch, current_iter):
        if hasattr(self, 'net_g_ema'):
            self.save_network([self.net_g,self.net_g_ema],'net_g',current_iter,param_key=['params','params_ema'])
        else:
            self.save_network(self.net_g,'net_g',current_iter)
        self.save_network(self.net_d1,'net_d1',current_iter)
        self.save_network(self.net_d2,'net_d2',current_iter)
        self.save_training_state(epoch,current_iter)