from glob import iglob
from shutil import copyfile
from pathlib import Path
from filecmp import cmp


remote_files = [
    'pipelines/*.ipynb',
    'pipelines/reports/*.ipynb',
]


def on_pre_build(config):
    '''Copy remote_files into docs tree'''
    dest_dir = Path('docs')

    for pattern in remote_files:
        files = iglob(pattern, recursive=True)
        for src in files:
            dest = dest_dir / src

            # Don't copy if the file is the same
            if dest.exists() and cmp(src, dest):
                continue

            # Create the parent path
            dest.parent.mkdir(parents=True, exist_ok=True)

            # Copy the src file to the dest
            copyfile(src, dest)


if __name__ == '__main__':
    on_pre_build(None)
