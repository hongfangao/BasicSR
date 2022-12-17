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
    os.makedirs('datasets/Rain13K/', exist_ok=True)
    if not is_file_equal('datasets/Rain13K/Rain13K_train_input.zip',
                         'ef7c988b2d015f03e49e14b4159e631a'):
        aligo.download('datasets/Rain13K/Rain13K_train_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_train_target.zip',
                         '072f50042d17ad04e92ee14a7c6ce04f'):
        aligo.download('datasets/Rain13K/Rain13K_train_target.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100_input.zip',
                         '32de3e0d5daeb7ae7c4ce36516db76a2'):
        aligo.download('datasets/Rain13K/Rain13K_test_100_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100_target.zip',
                         'ddbcbe8c3b99388656a555481b3d90b0'):
        aligo.download('datasets/Rain13K/Rain13K_test_100_target.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100L_input.zip',
                         '776a3f732dd96eaa0ee2932cd151b42d'):
        aligo.download('datasets/Rain13K/Rain13K_test_100L_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100L_target.zip',
                         '109561e31d5cfb808732b83aa923d922'):
        aligo.download('datasets/Rain13K/Rain13K_test_100L_target.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100H_input.zip',
                         '8159dc10550f9915357f6aa102f50470'):
        aligo.download('datasets/Rain13K/Rain13K_test_100H_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_100H_target.zip',
                         '51dcd36b4af1204cb7ff5f7c18050974'):
        aligo.download('datasets/Rain13K/Rain13K_test_100H_target.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_1200_input.zip',
                         '514afb2b7625234787973ad4faeae156'):
        aligo.download('datasets/Rain13K/Rain13K_test_1200_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_1200_target.zip',
                         'ba9ca8b64f55b0437e2a11024dc29d6e'):
        aligo.download('datasets/Rain13K/Rain13K_test_1200_target.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_2800_input.zip',
                         '265c526b27e680b37b08ce6bb3add8c4'):
        aligo.download('datasets/Rain13K/Rain13K_test_2800_input.zip',
                       'datasets/Rain13K/')
    if not is_file_equal('datasets/Rain13K/Rain13K_test_2800_target.zip',
                         '8d0c63834a25341272e6f3af016a74d3'):
        aligo.download('datasets/Rain13K/Rain13K_test_2800_target.zip',
                       'datasets/Rain13K/')
