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


class SourceFolderNotExistsError(Exception):
    def __init__(self):
        super().__init__('Source folder not exists or not a folder')


class DestinationFolderNotExistsError(Exception):
    def __init__(self):
        super().__init__('Destination folder not exists or not a folder')


class SourceParameterError(Exception):
    def __init__(self):
        super().__init__('Source folder information required. Example : script.py "source folder"')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser("File Copier")
        parser.add_argument('--src', help="Source Directory")
        parser.add_argument(
            '--dst', help="Destination Directory")
        args = parser.parse_args()

        if args.src is None or args.src == "":
            raise SourceParameterError()
        else:
            src = Path(args.src)

        if args.dst is None or args.dst == "":
            dst = Path('./dist')
            if not dst.exists():
                dst.mkdir()
        else:
            dst = Path(args.dst)

        if not src.exists() or not src.is_dir():
            raise SourceFolderNotExistsError()

        if not dst.exists() or not dst.is_dir():
            raise DestinationFolderNotExistsError()

        copyFiles(src, dst)
        print('Files copied!')

    except Exception as e:
        print(e)

# sudo python3 goit-algo-hw-03-1.py "src" -> Files will be copied same directory with script under "dist" folder.
# sudo python3 goit-algo-hw-03-1.py "src dir" --dst "dst dir"
