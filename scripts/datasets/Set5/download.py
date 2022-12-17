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
    if is_file_equal('datasets/Set5.zip', '4395d7e7e6d7ac5c9cb2a8b2acbdba5d'):
        print('Set5.zip already exists.')
    else:
        aligo.download('datasets/Set5.zip', 'datasets/')
