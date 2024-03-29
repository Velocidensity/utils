# Utils
An assorted collection of simple utility scripts for day-to-day use.

## S(ym)l(ink)

```
usage: sl [-h] [-H] [input ...] output

positional arguments:
  input       Input file(s)
  output      Output path

options:
  -h, --help  show this help message and exit
  -H          Create a hard link (default is soft link)
```

Why not use regular `ln -s`?
- it does not resolve paths, so unless you pretty much have to use absolute paths to get it to work as intended
- linking multiple files works only with wildcards (e.g. `ln -s data_* www/` and not `ln -s data_1.txt data_2.txt www/`)
- this script defaults to soft linking, so it's slightly shorter to type :P

## Nextcloud uploader

```
usage: nextcloud_upload.py [-h] [file [file ...]]

Nextcloud uploader

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit

```

Requirements: [tqdm](https://github.com/tqdm/tqdm), [rich](https://github.com/Textualize/rich), [httpx](https://github.com/encode/httpx/)
