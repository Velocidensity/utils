#!/usr/bin/python3
import argparse
from pathlib import Path
from typing import Iterable

import httpx
import rich.progress
from tqdm.utils import CallbackIOWrapper

# USER CONFIGURATION #
URL = 'https://DOMAIN/remote.php/webdav/DIRECTORY/{name}'
CREDS = 'username:password'
# USER CONFIGURATION #


class IterableCallbackIOWrapper(CallbackIOWrapper, Iterable):
    def __iter__(self, *args, **kwargs):
        return self.stream.__iter__(*args, **kwargs)


def upload(file: Path):
    with rich.progress.Progress(
        "[progress.percentage]{task.percentage:>3.0f}%",
        rich.progress.BarColumn(bar_width=69),
        rich.progress.DownloadColumn(),
        rich.progress.TransferSpeedColumn(),
    ) as progress:
        task1 = progress.add_task("[green]Uploading...", total=file.stat().st_size)

        def update(value):
            progress.update(task1, advance=value)

        with file.open(mode='rb') as f:
            wrapped_file = IterableCallbackIOWrapper(update, f, "read")
            httpx.put(URL.format(name=file.name), data=wrapped_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nextcloud uploader")
    parser.add_argument(
        'file',
        nargs='*',
        type=Path
    )
    args = parser.parse_args()
    for file in args.file:
        if not file.exists():
            print(f'{file} could not be found!')
            continue

        print(f'Uploading {file}...')
        upload(file)
