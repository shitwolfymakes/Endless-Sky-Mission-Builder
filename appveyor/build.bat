REM Add our desired Python installation the *beginning* of the PATH, so the "python" command refers to this executable.
REM It HAS to be 3.7+, otherwise PyInstaller binaries will have import errors for some reason.
REM Also add its "Scripts" folder, which will contain the PyInstaller executable once installed.
set PATH=C:\Python37-x64;C:\Python37-x64\Scripts;%PATH%

REM Setup required Packages
python -m pip install PyInstaller
python -m pip install -r requirements.txt

REM Build a directory distribution ("-D") with PyInstaller
REM We have to add the data folder here since it won't be added automatically. See utils/loadtooltips.py for an example of how to access it
pyinstaller -D --noconfirm --noconsole --icon .\icon.ico --hidden-import ttkthemes --add-data ".\src\data;data" .\src\ESMB.py
REM Archive with maximum zip compression
7z a -tzip -mx9 -y .\ESMB-win64-pyinstaller.zip .\dist\ESMB
REM Cleanup
RD /S /Q dist

REM Build a OneFile executable ("-F") with PyInstaller
pyinstaller -F --noconfirm --noconsole --icon .\icon.ico --hidden-import ttkthemes --add-data ".\src\data;data" .\src\ESMB.py
COPY .\dist\ESMB.exe .\ESMB-win64-pyinstaller.exe
REM Cleanup
RD /S /Q dist