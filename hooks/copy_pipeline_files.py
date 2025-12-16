from glob import iglob
from shutil import copyfile, rmtree
from pathlib import Path
from filecmp import cmp

UPSTREAM = 'upstream/pipelines/'
dest_dir = Path('docs/pipelines')

remote_files = [
    'catalogue.ipynb',
    'combine.ipynb',
    'cultural-learning.ipynb',
    'digital-audience.ipynb',
    'digital-events.ipynb',
    'digital-followers.ipynb',
    'manual_data_feeds.ipynb',
    'programme.ipynb',
    'publish.ipynb',
    'reports.ipynb',
    'status.ipynb',
    'audience-survey.ipynb',
    'sustainability.ipynb',
    'ticketing.ipynb',
    'volunteer-people.ipynb',
    'volunteer-shift.ipynb',
    'youth-skills.ipynb',
    # 'reports/*.ipynb',
]

def on_startup(command, dirty):
    '''Clear target directory to ensure stuff not left lying around'''
    rmtree(dest_dir, ignore_errors=True)

def on_pre_build(config):
    '''Copy remote_files into docs tree'''

    for pattern in remote_files:
        files = iglob(f'{UPSTREAM}{pattern}', recursive=False)
        for src in files:
            print(src)
            dest = dest_dir / src.replace(UPSTREAM, '')

            # Don't copy if the file is the same
            if dest.exists() and cmp(src, dest):
                continue

            # Create the parent path
            dest.parent.mkdir(parents=True, exist_ok=True)

            # Copy the src file to the dest
            copyfile(src, dest)


if __name__ == '__main__':
    on_pre_build(None)
