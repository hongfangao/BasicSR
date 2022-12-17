''' publish model '''
import os
from argparse import ArgumentParser

import torch
from falcon.utils import aligo


def parse_args():
    ''' parse_args '''
    parser = ArgumentParser()
    parser.add_argument('--input',
                        type=str,
                        required=True,
                        help='Path to input model path.')
    parser.add_argument('--output',
                        type=str,
                        required=True,
                        help='Path to output model path.')
    args = parser.parse_args()
    args.floder = args.output.replace(os.path.basename(args.output), '')
    return args


def publish():
    ''' publish '''
    args = parse_args()

    # load models
    model = torch.load(args.input, map_location=torch.device('cpu'))

    # save
    os.makedirs(args.floder, exist_ok=True)
    torch.save(model, args.output)
    aligo.upload_file(args.output, args.floder)


if __name__ == '__main__':
    publish()
