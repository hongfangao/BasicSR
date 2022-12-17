''' create lmdb '''
from falcon.utils import scandir
from falcon.utils.lmdb import make_lmdb_from_imgs


def prepare_keys_sidd(folder_path):
    """Prepare image path list and keys for SIDD dataset.
    Args:
        folder_path (str): Folder path.
    Returns:
        list[str]: Image path list.
        list[str]: Key list.
    """
    print('Reading image path list ...')
    img_path_list = sorted(
        list(scandir(folder_path, suffix='png', recursive=False)))
    keys = [img_path.split('.png')[0] for img_path in sorted(img_path_list)]
    return img_path_list, keys


def create_lmdb_for_sidd():
    """ Create lmdb files for SIDD dataset. """
    # HR images
    folder_path = 'datasets/GoPro/train/sharp/subs'
    lmdb_path = 'datasets/GoPro/train/sharp/subs.lmdb'
    img_path_list, keys = prepare_keys_sidd(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    folder_path = 'datasets/GoPro/train/blur/subs'
    lmdb_path = 'datasets/GoPro/train/blur/subs.lmdb'
    img_path_list, keys = prepare_keys_sidd(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    folder_path = 'datasets/GoPro/train/blur_gamma/subs'
    lmdb_path = 'datasets/GoPro/train/blur_gamma/subs.lmdb'
    img_path_list, keys = prepare_keys_sidd(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)


if __name__ == '__main__':
    create_lmdb_for_sidd()
