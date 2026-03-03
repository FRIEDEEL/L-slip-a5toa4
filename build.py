# build.py

import PyInstaller.__main__

PyInstaller.__main__.run([
    "src/a5toa4/qtfront/app.py",
    "--name=A5toA4",
    "--windowed",
    "--onefile",
    "--clean",
    "--noconfirm",
])