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
    os.makedirs('datasets/SIDD/', exist_ok=True)
    aligo.download('datasets/SIDD/SIDD_Medium_Srgb.zip', 'datasets/SIDD/')
    aligo.download('datasets/SIDD/ValidationGtBlocksSrgb.mat',
                   'datasets/SIDD/')
    aligo.download('datasets/SIDD/ValidationNoisyBlocksSrgb.mat',
                   'datasets/SIDD/')
