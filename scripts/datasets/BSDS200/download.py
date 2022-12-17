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
    os.makedirs('datasets/BSDS200/', exist_ok=True)
    if is_file_equal('datasets/BSDS200.zip',
                     '8267d3cadc5dfbebb26770609bac8cb0'):
        print('BSDS200.zip already exists.')
    else:
        aligo.download('datasets/BSDS200.zip', 'datasets/')
