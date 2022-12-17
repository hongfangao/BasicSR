''' SIDD regroup '''
import os

from falcon.utils import scandir


def main():
    ''' main '''
    base_path = 'datasets/SIDD/'
    paths = scandir(os.path.join(base_path, 'SIDD_Medium_Srgb/Data'),
                    recursive=True)
    input_paths = [path for path in paths if 'NOISY' in path]
    target_paths = [path for path in paths if 'GT' in path]
    for path in input_paths:
        os.system(
            f'mv {os.path.join(base_path, "SIDD_Medium_Srgb/Data", path)} {os.path.join(base_path, "train/input/original/", os.path.basename(path).lower())}'
        )
    for path in target_paths:
        os.system(
            f'mv {os.path.join(base_path, "SIDD_Medium_Srgb/Data", path)} {os.path.join(base_path, "train/target/original/", os.path.basename(path).lower())}'
        )


if __name__ == '__main__':
    main()
