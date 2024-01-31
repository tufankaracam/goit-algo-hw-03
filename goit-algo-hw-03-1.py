import os
import argparse
from pathlib import Path
from shutil import copy2


def copyFiles(src: Path, dst: Path):

    for item in src.iterdir():
        if item.is_dir():
            copyFiles(item, dst)
        else:
            if not item.name.startswith('.DS_Store'):
                suffixpath = dst.joinpath(item.suffix.replace('.', ''))
                if not suffixpath.exists():
                    suffixpath.mkdir()
                copy2(str(item), suffixpath,)
                print(f'{str(item)} is copied to {str(suffixpath)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("File Copier")
    parser.add_argument('src', help="Source Directory")
    parser.add_argument(
        '--dst', help="Destination Directory", default="./dist")
    args = parser.parse_args()
    src = Path(args.src)
    dst = Path(args.dst)

    print(dst)

    if not src.is_dir():
        print('Source is not a directory!')
        exit()

    if not dst.exists() or not dst.is_dir():
        if (args.dst == './dist'):
            dst.mkdir()
        else:
            print('Destination is not a directory!')
            exit()

    copyFiles(src, dst)


# sudo python3 goit-algo-hw-03-1.py "src"
# sudo python3 goit-algo-hw-03-1.py "src dir" --dst "dst dir"
