''' DF2K '''
import os

from falcon.utils import aligo
from falcon.utils.hash import get_file_md5


def is_file_equal(path, md5):
    ''' is_file_equal '''
    if os.path.exists(path):
        if md5 == get_file_md5(path, max_iter=5000):
            return True
        os.remove(path)
        return False
    return False


if __name__ == '__main__':
    os.makedirs('datasets/DF2K/', exist_ok=True)
    if not is_file_equal('datasets/Flickr2K.tar',
                         '66e4ccdcfacc055fa0758b0ad0ea3558'):
        aligo.download('datasets/Flickr2K.tar', 'datasets/')
