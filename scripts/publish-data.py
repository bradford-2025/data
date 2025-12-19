'''
Script to grab data from the upstream repository and publish it

Relies on files being defined
'''
from pathlib import Path
from shutil import copyfile

import logging

import yaml

logger = logging.getLogger(__file__)

ROOT = (Path(__file__).parent / "..").resolve()
UPSTREAM_DATA = ROOT / "upstream/data"
TARGET = ROOT / "docs/datasets"


def publish_data():
    with open(UPSTREAM_DATA / "reference/published.yaml", encoding="utf-8") as config:
        files = yaml.load(config, Loader=yaml.BaseLoader)
    if not files:
        return
    for src, dst in ((UPSTREAM_DATA / "published" / f, TARGET / f) for f in files):
        if not src.exists():
            logger.error(f'File does not exist {src}')
            continue
        dst.parent.mkdir(exist_ok=True, parents=True)
        copyfile(src, dst)


if __name__ == "__main__":
    publish_data()
