import torch
from torch import nn
import torch.nn.functional as F

from basicsr.utils.registry import ARCH_REGISTRY

class Upsample(nn.Module):
    def __init__(self,scale,num_feat):
        super().__init__()
        self.conv1 = nn.Conv2d(num_feat,num_feat*scale**2,3,1,1)
        self.conv2 = nn.Conv2d(num_feat,num_feat,3,1,1)
        self.scale = scale
    def forward(self,x):
        out = self.conv1(x)
        out = F.pixel_shuffle(out,self.scale)
        out = self.conv2(out)
        return out

class DWConv(nn.Module):
    def __init__(self,dim):
        super().__init__()
        self.conv = nn.Conv2d(dim,dim,3,1,1,groups=dim)
    def forward(self,x):
        return self.conv(x)

class ResidualBlockNoBN(nn.Module):
    def __init__(self,in_channels,res_scale):
        super().__init__()
        self.res_scale = res_scale
        self.conv1 = nn.Conv2d(in_channels,in_channels,3,1,1)
        self.conv2 = nn.Conv2d(in_channels,in_channels,3,1,1)
        self.gelu = nn.GELU()
    def forward(self,x):
        identity = x
        out = self.conv1(x)
        out = self.gelu(out)
        out = self.conv2(out)
        return identity + self.res_scale * out

class SELayer(nn.Module):
    def __init__(self,channel,reduction=16):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel,channel//reduction,bias=False),
            nn.GELU(),
            nn.Linear(channel//reduction,channel,bias=False),
            nn.Sigmoid()
        )
    def forward(self,x):
        n,c,_,_ = x.size()
        out = self.avg_pool(x).view(n,c)
        out = self.fc(out).view(n,c,1,1)
        return x * out.expand_as(x)

'''
dilated convolution with different dilation factor
'''

class DilatedResidualConv(nn.Module):
    def __init__(self,in_channels = 32,out_channels = 32,dilation = 1):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(in_channels,out_channels,3,1,padding=dilation,dilation=dilation),
            nn.GELU(),
            nn.Conv2d(in_channels,out_channels,3,1,padding=dilation,dilation=dilation),
            SELayer(out_channels,reduction=16)
        )

    def forward(self,x):
        return x + self.body(x)

class FuseBlock(nn.Module):
    def __init__(self,channels):
        super().__init__()
        self.body = nn.Sequential(
            nn.Linear(channels*2,channels,bias=True),
            nn.GELU()
        )
    def forward(self,x,y):
        b, c, h ,w = x.shape
        x = x.permute(0,2,3,1).contiguous().view(-1,c)
        y = y.permute(0,2,3,1).contiguous().view(-1,c)
        out = self.body(torch.cat((x,y),dim=-1))
        out = out.view(b,h,w,c).permute(0,3,1,2)
        return out


class TreeResidualEncoder(nn.Module):
    def __init__(self,in_channels,out_channels):
        super().__init__()
        self.out_channels = out_channels
        self.dilated_models = nn.ModuleList([DilatedResidualConv(in_channels,out_channels,dilation=d) for d in range(1,5)])
        self.fuse12 = FuseBlock(out_channels)
        self.fuse34 = FuseBlock(out_channels)
        self.fuse = FuseBlock(out_channels)
    def forward(self,x):
        fs = [model(x) for model in self.dilated_models]
        fs = self.fuse(self.fuse12(fs[0],fs[1]),self.fuse34(fs[2],fs[3]))
        fs = fs + x
        return fs

class Encoder(nn.Module):
    def __init__(self,in_channels,out_channels):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(in_channels,out_channels,3,1,1),
            TreeResidualEncoder(out_channels,out_channels),
            nn.Conv2d(out_channels,2*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*2,out_channels*2),
            nn.Conv2d(2*out_channels,3*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*3,out_channels*3),
            nn.Conv2d(3*out_channels,4*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*4,out_channels*4),
            nn.Conv2d(4*out_channels,5*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*5,out_channels*5),
            nn.Conv2d(5*out_channels,6*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*6,out_channels*6),
            nn.Conv2d(6*out_channels,6*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*6,out_channels*6),
            nn.Conv2d(6*out_channels,6*out_channels,3,1,1),
            TreeResidualEncoder(out_channels*6,out_channels*6),
        )
    def forward(self,x):
        return self.body(x)

class Decoder(nn.Module):
    def __init__(self,in_channels,out_channels):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(6*in_channels,6*out_channels,3,1,1),
            TreeResidualEncoder(6*out_channels,6*out_channels),
            nn.Conv2d(6*out_channels,6*out_channels,3,1,1),
            TreeResidualEncoder(6*out_channels,6*out_channels),
            nn.Conv2d(6*out_channels,5*out_channels,3,1,1),
            TreeResidualEncoder(5*out_channels,5*out_channels),
            nn.Conv2d(5*out_channels,4*out_channels,3,1,1),
            TreeResidualEncoder(4*out_channels,4*out_channels),
            nn.Conv2d(4*out_channels,3*out_channels,3,1,1),
            TreeResidualEncoder(3*out_channels,3*out_channels),
            nn.Conv2d(3*out_channels,2*out_channels,3,1,1),
            TreeResidualEncoder(2*out_channels,2*out_channels),
            nn.Conv2d(2*out_channels,out_channels,3,1,1),
            TreeResidualEncoder(out_channels,out_channels)
        )
    def forward(self,x):
        return self.body(x)

@ARCH_REGISTRY.register()
class WAEOPGANGenerator(nn.Module):
    def __init__(self,in_channels=3,out_channels=32,scale=2):
        super().__init__()
        self.scale = scale
        self.encoder = Encoder(in_channels,out_channels)
        # self.latent = nn.Sequential(
        #     ResidualBlockNoBN(out_channels*6,1),
        #     ResidualBlockNoBN(out_channels*6,1),
        #     ResidualBlockNoBN(out_channels*6,1),
        #     ResidualBlockNoBN(out_channels*6,1),
        #     ResidualBlockNoBN(out_channels*6,1),
        # )
        self.decoder = nn.Sequential(
            Decoder(out_channels,out_channels),
            nn.Conv2d(out_channels,out_channels,3,1,1),
            Upsample(scale,out_channels),
            nn.Conv2d(out_channels,in_channels,3,1,1),
        )
    def forward(self,x):
        latent_x = self.encoder(x)
        # latent_x = self.latent(latent_x)
        # mean = torch.mean(latent_x)
        # var = torch.std(latent_x)
        out = self.decoder(latent_x)
        # return out, latent_x, mean, var
        return out
