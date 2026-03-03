# L-classification slip a5-to-a4 converter
Version 0.2.0
## Overview
This program process A5-size slips (downloaded from L-classification website) and append them twice to A4 size pages and generate PDF file for printing.

## Installation
First, make sure a proper python version (>=3.12) is installed in your computer.

This project is not released to PyPI.
So you have to manually clone the repo to your computer.

### Downloading
Download by cloning this repo.
Use `git clone` or just download `.zip` file and unzip it.

### (Optional) Install with `pip`
Change to the root directory of this repo.

Then use pip to install this library:

`pip install -e .`

### (Optional) Wrap with `pyinstaller`
Use `pyinstaller` to wrap the program to a `.app` / `.exe` runnable application.

Under the root directory of this repo, run
```shell
python build.py
```

You will get a executable file (`.exe` under Windows or `.app` under MacOS) at `dist/` subdirectory.

You can just copy it to anywhere and simply run the program by double clicking it.


## Usage
Under the root directory
```shell
python -m a5toa4.qtfront.app
```

