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
    os.makedirs('datasets/', exist_ok=True)
    if is_file_equal('datasets/Set14.zip', 'efe68a0553772ace8b1c59cf8496b6f6'):
        print('Set14.zip already exists.')
    else:
        aligo.download('datasets/Set14.zip', 'datasets/')
