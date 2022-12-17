''' create lmdb '''
from falcon.utils import scandir
from falcon.utils.lmdb import make_lmdb_from_imgs


def prepare_keys_df2k(folder_path):
    """Prepare image path list and keys for DF2K dataset.
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


def create_lmdb_for_df2k():
    """ Create lmdb files for DF2K dataset. """
    # HR images
    folder_path = 'datasets/DF2K/train/HR/subs'
    lmdb_path = 'datasets/DF2K/train/HR/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx2 images
    folder_path = 'datasets/DF2K/train/LR/bicubic/X2/subs'
    lmdb_path = 'datasets/DF2K/train/LR/bicubic/X2/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx3 images
    folder_path = 'datasets/DF2K/train/LR/bicubic/X3/subs'
    lmdb_path = 'datasets/DF2K/train/LR/bicubic/X3/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DF2K/train/LR/bicubic/X4/subs'
    lmdb_path = 'datasets/DF2K/train/LR/bicubic/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx2 images
    folder_path = 'datasets/DF2K/train/LR/unknown/X2/subs'
    lmdb_path = 'datasets/DF2K/train/LR/unknown/X2/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx3 images
    folder_path = 'datasets/DF2K/train/LR/unknown/X3/subs'
    lmdb_path = 'datasets/DF2K/train/LR/unknown/X3/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DF2K/train/LR/unknown/X4/subs'
    lmdb_path = 'datasets/DF2K/train/LR/unknown/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_df2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)


if __name__ == '__main__':
    create_lmdb_for_df2k()
