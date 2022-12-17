''' publish model '''
import os
from argparse import ArgumentParser

from falcon.utils import aligo, hash


def parse_args():
    ''' parse_args '''
    parser = ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='model type.')
    args = parser.parse_args()
    return args


def get_info():
    ''' get info '''
    return {
        'EDSR-x2': {
            'file': 'EDSR_Lx2_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/EDSR/',
            'floder': 'experiments/pretrained_models/EDSR/',
            'md5sum': '0424d68f73106267930b49a3ac7df69b'
        },
        'EDSR-x3': {
            'file': 'EDSR_Lx3_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/EDSR/',
            'floder': 'experiments/pretrained_models/EDSR/',
            'md5sum': 'e267b073d2e0bc4c681404ec48385a09'
        },
        'EDSR-x4': {
            'file': 'EDSR_Lx4_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/EDSR/',
            'floder': 'experiments/pretrained_models/EDSR/',
            'md5sum': '0200c6d2f95069ba6a889194da4728d7'
        },
        'EDSRM-x2': {
            'file': 'EDSRM_Lx2_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/EDSR/',
            'floder': 'experiments/pretrained_models/EDSR/',
            'md5sum': '4ff8e5bdfc6306ec7c529a5a4c5a7a4c'
        },
        'ECBSR-x2-M4C8': {
            'file': 'ECBSR_M4C8_x2_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/ECBSR/',
            'floder': 'experiments/pretrained_models/ECBSR/',
            'md5sum': '5f29d88372e3b5e85e8173afc4d2a36e'
        },
        'ECBSR-x4-M4C8': {
            'file': 'ECBSR_M4C8_x4_DIV2K.pth',
            'aligo': 'experiments/pretrained_models/ECBSR/',
            'floder': 'experiments/pretrained_models/ECBSR/',
            'md5sum': 'bb2c89c684bb7394b8fc11dae525bb8e'
        },
    }


def publish():
    ''' publish '''
    args = parse_args()
    info = get_info()[args.model]

    if not os.path.exists(os.path.join(
            info['floder'], info['file'])) or hash.get_file_md5(
                os.path.join(info['floder'], info['file'])) != info['md5sum']:
        aligo.download(os.path.join(info['aligo'], info['file']),
                       info['floder'])
        assert hash.get_file_md5(os.path.join(info['floder'],
                                              info['file'])) == info['md5sum']


if __name__ == '__main__':
    publish()
