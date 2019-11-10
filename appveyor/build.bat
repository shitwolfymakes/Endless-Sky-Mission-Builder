REM Add our desired Python installation the *beginning* of the PATH, so the "python" command refers to this executable.
REM Also add its "Scripts" folder, which will contain the PyInstaller executable once installed.
set PATH=C:\Python37-x64;C:\Python37-x64\Scripts;%PATH%

REM Setup required Packages
python -m pip install nuitka PyInstaller
python -m pip install -r requirements.txt

REM Switch to our source directory
PUSHD .\src
REM Now that we are in ".\src", paths relative to the top level have to be prefixed with "..\", e.g. "..\icon.ico"

REM Nuitka Compilation
REM We use "--mingw64" because i trust in it to be available more than clang, which would be the default
REM The two plugin-related arguments are responsible for copying all required tkinter- and ttkthemes-files to the final distribution folder
python -m nuitka --assume-yes-for-downloads --standalone --show-progress --mingw64 --show-scons --user-plugin=..\appveyor\ttkthemes_nuitka_plugin.py --plugin-enable=tk-inter --windows-disable-console --windows-icon=..\icon.ico .\ESMB.py
MOVE .\ESMB.dist .\ESMB
REM Archive with maximum zip compression
7z a -tzip -mx9 -y ..\ESMB-win64-nuitka.zip .\ESMB\
REM Cleanup
RD /S /Q ESMB

REM Build a directory distribution ("-D") with PyInstaller
pyinstaller -D --noconfirm --noconsole --icon ..\icon.ico --hidden-import ttkthemes .\ESMB.py
REM Archive with maximum zip compression
7z a -tzip -mx9 -y ..\ESMB-win64-pyinstaller.zip .\dist\ESMB
REM Cleanup
RD /S /Q dist

REM Build a OneFile executable ("-F") with PyInstaller
pyinstaller -F --noconfirm --noconsole --icon ..\icon.ico --hidden-import ttkthemes .\ESMB.py
COPY .\dist\ESMB.exe ..\ESMB-win64-pyinstaller.exe
REM Cleanup
RD /S /Q dist

REM Return to top level, just to be sure
POPD