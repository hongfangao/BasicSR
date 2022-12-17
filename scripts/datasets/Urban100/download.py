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
    os.makedirs('datasets/Urban100/', exist_ok=True)

    if not is_file_equal('datasets/urban100.zip',
                         'b2f6deb6a4be7cef1cf92cf99a45ad85'):
        aligo.download('datasets/urban100.zip', 'datasets/')
