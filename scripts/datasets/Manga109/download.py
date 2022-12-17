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
    os.makedirs('datasets/Manga109/', exist_ok=True)

    if not is_file_equal('datasets/manga109.zip',
                         'f0a2d6384b0e450bc5ff9e01610fecc0'):
        aligo.download('datasets/manga109.zip', 'datasets/')
