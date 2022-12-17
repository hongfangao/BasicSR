''' publish model '''
import os
import sys
from argparse import ArgumentParser

import torch
from falcon.utils import aligo

try:
    from core.archs.ir.ECBSR.arch import ECBSR, ECBSRT
except Exception:
    sys.path.extend([
        path.replace('/scripts/publish_model', '') for path in sys.path
        if 'scripts/publish_model' in path
    ])
    from core.archs.ir.ECBSR.arch import ECBSR, ECBSRT


def parse_args():
    ''' parse_args '''
    parser = ArgumentParser()
    parser.add_argument('--num_in_ch',
                        type=int,
                        required=True,
                        help='number of in channel.')
    parser.add_argument('--num_out_ch',
                        type=int,
                        required=True,
                        help='number of out channel.')
    parser.add_argument('--upscale',
                        type=int,
                        required=True,
                        help='upsample scale.')
    parser.add_argument('--num_block',
                        type=int,
                        required=True,
                        help='number of blocks.')
    parser.add_argument('--num_feat',
                        type=int,
                        required=True,
                        help='number of features.')
    parser.add_argument('--act_type',
                        type=str,
                        required=True,
                        help='type of activation.')
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
    model1 = ECBSR(args.num_in_ch, args.num_out_ch, args.upscale,
                   args.num_block, args.num_feat, args.act_type)
    model2 = ECBSRT(args.num_in_ch, args.num_out_ch, args.upscale,
                    args.num_block, args.num_feat, args.act_type)
    model1.load_state_dict(
        torch.load(args.input, map_location=torch.device('cpu')))

    # rep
    for backbone1, backbone2 in zip(model1.backbone, model2.backbone):
        weight, bias = backbone1.rep_params()
        backbone2[0].weight.data = weight
        backbone2[0].bias.data = bias
        if hasattr(backbone1, 'act') and hasattr(backbone1.act, 'weight'):
            backbone2[1].weight.data = backbone1.act.weight.data
    state = model2.state_dict()

    # test
    input = torch.rand(32, 1, 64, 64)
    model1.eval()
    output1 = model1(input)
    output2 = model2(input)
    assert torch.allclose(output1, output2)

    # save
    os.makedirs(args.floder, exist_ok=True)
    torch.save(state, args.output)
    aligo.upload_file(args.output, args.floder)


if __name__ == '__main__':
    publish()
