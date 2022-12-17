''' create lmdb '''
from falcon.utils import scandir
from falcon.utils.lmdb import make_lmdb_from_imgs


def prepare_keys_div2k(folder_path):
    """Prepare image path list and keys for DIV2K dataset.
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


def create_lmdb_for_div2k():
    """ Create lmdb files for DIV2K dataset. """
    # HR images
    folder_path = 'datasets/DIV2K/train/HR/subs'
    lmdb_path = 'datasets/DIV2K/train/HR/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx2 images
    folder_path = 'datasets/DIV2K/train/LR/bicubic/X2/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/bicubic/X2/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx3 images
    folder_path = 'datasets/DIV2K/train/LR/bicubic/X3/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/bicubic/X3/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DIV2K/train/LR/bicubic/X4/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/bicubic/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx8 images
    folder_path = 'datasets/DIV2K/train/LR/bicubic/X8/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/bicubic/X8/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx2 images
    folder_path = 'datasets/DIV2K/train/LR/unknown/X2/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/unknown/X2/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx3 images
    folder_path = 'datasets/DIV2K/train/LR/unknown/X3/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/unknown/X3/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DIV2K/train/LR/unknown/X4/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/unknown/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DIV2K/train/LR/difficult/X4/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/difficult/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DIV2K/train/LR/wild/X4/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/wild/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)

    # LRx4 images
    folder_path = 'datasets/DIV2K/train/LR/mild/X4/subs'
    lmdb_path = 'datasets/DIV2K/train/LR/mild/X4/subs.lmdb'
    img_path_list, keys = prepare_keys_div2k(folder_path)
    make_lmdb_from_imgs(folder_path, lmdb_path, img_path_list, keys)


if __name__ == '__main__':
    create_lmdb_for_div2k()
