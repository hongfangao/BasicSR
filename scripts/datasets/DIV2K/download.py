''' download '''
import os

from falcon.utils import aligo
from falcon.utils.hash import get_file_md5


def is_file_equal(path, md5):
    ''' is_file_equal '''
    if os.path.exists(path):
        if md5 == get_file_md5(path):
            return True
        os.remove(path)
        return False
    return False


if __name__ == '__main__':
    os.makedirs('datasets/DIV2K/', exist_ok=True)
    # train
    if not is_file_equal('datasets/DIV2K/DIV2K_train_HR.zip',
                         'bdc2d9338d4e574fe81bf7d158758658'):
        aligo.download('datasets/DIV2K/DIV2K_train_HR.zip', 'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_bicubic_X2.zip',
                         '9a637d2ef4db0d0a81182be37fb00692'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_bicubic_X2.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_unknown_X2.zip',
                         '1396d023072c9aaeb999c28b81315233'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_unknown_X2.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_bicubic_X3.zip',
                         'ad80b9fe40c049a07a8a6c51bfab3b6d'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_bicubic_X3.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_unknown_X3.zip',
                         '4e651308aaa54d917fb1264395b7f6fa'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_unknown_X3.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_bicubic_X4.zip',
                         '76c43ec4155851901ebbe8339846d93d'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_bicubic_X4.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_unknown_X4.zip',
                         'e3c7febb1b3f78bd30f9ba15fe8e3956'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_unknown_X4.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_x8.zip',
                         '613db1b855721b3d2b26f4194a1d22a6'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_x8.zip',
                       'datasets/DIV2K/')

    # valid
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_HR.zip',
                         '9fcdda83005c5e5997799b69f955ff88'):
        aligo.download('datasets/DIV2K/DIV2K_valid_HR.zip', 'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_bicubic_X2.zip',
                         '1512c9a3f7bde2a1a21a73044e46b9cb'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_bicubic_X2.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_unknown_X2.zip',
                         'd319bd9033573d21de5395e6454f34f8'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_unknown_X2.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_bicubic_X3.zip',
                         '18b1d310f9f88c13618c287927b29898'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_bicubic_X3.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_unknown_X3.zip',
                         '05184168e3608b5c539fbfb46bcade4f'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_unknown_X3.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_bicubic_X4.zip',
                         '21962de700c8d368c6ff83314480eff0'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_bicubic_X4.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_unknown_X4.zip',
                         '8ac3413102bb3d0adc67012efb8a6c94'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_unknown_X4.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_x8.zip',
                         'c5aeea2004e297e9ff3abfbe143576a5'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_x8.zip',
                       'datasets/DIV2K/')

    # real difficult
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_difficult.zip',
                         '5a8f2b9e0c5f5ed0dac271c1293662f4'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_difficult.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_difficult.zip',
                         '1620af11bf82996bc94df655cb6490fe'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_difficult.zip',
                       'datasets/DIV2K/')

    # real wild
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_wild.zip',
                         'd00982366bffee7c4739ba7ff1316b3b'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_wild.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_wild.zip',
                         'aacae8db6bec39151ca5bb9c80bf2f6c'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_wild.zip',
                       'datasets/DIV2K/')

    # real mild
    if not is_file_equal('datasets/DIV2K/DIV2K_train_LR_mild.zip',
                         '807b3e3a5156f35bd3a86c5bbfb674bc'):
        aligo.download('datasets/DIV2K/DIV2K_train_LR_mild.zip',
                       'datasets/DIV2K/')
    if not is_file_equal('datasets/DIV2K/DIV2K_valid_LR_mild.zip',
                         '8c433f812ca532eed62c11ec0de08370'):
        aligo.download('datasets/DIV2K/DIV2K_valid_LR_mild.zip',
                       'datasets/DIV2K/')
