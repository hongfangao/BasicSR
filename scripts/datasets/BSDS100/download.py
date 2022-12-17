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
    os.makedirs('datasets/BSDS100/', exist_ok=True)
    if is_file_equal('datasets/BSDS100.zip',
                     '5ce69a089ae1c1195d3344c9f26eeef8'):
        print('BSDS100.zip already exists.')
    else:
        aligo.download('datasets/BSDS100.zip', 'datasets/')
