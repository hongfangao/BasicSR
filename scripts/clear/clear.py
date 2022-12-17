''' clear '''
import os
import shutil


def dfs_remove(base='./', ):
    ''' dfs_remove '''
    pths = os.listdir(base)
    for pth in pths:
        if pth == 'datasets':
            continue
        pth = os.path.join(base, pth)
        if os.path.isdir(pth):
            if pth.endswith('__pycache__') or pth.startswith('debug_'):
                print(f'{pth} will be remove.')
                shutil.rmtree(pth)
            else:
                dfs_remove(pth)


if __name__ == '__main__':
    dfs_remove()
