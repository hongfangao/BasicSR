''' GoPro regroup '''
import os


def main():
    ''' main '''
    for md in ['train', 'test']:
        names = [
            p for p in os.listdir(f'datasets/GoPro/{md}/')
            if p not in ['sharp', 'blur', 'blur_gamma']
        ]
        for name in names:
            for mode in ['sharp', 'blur', 'blur_gamma']:
                paths = os.listdir(f'datasets/GoPro/{md}/{name}/{mode}/')
                for path in paths:
                    os.system(
                        f'mv datasets/GoPro/{md}/{name}/{mode}/{path} datasets/GoPro/{md}/{mode}/{name}_{path} '
                    )


if __name__ == '__main__':
    main()
