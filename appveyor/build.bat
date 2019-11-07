REM Setup
C:\Python37-x64\python -m pip install nuitka PyInstaller
C:\Python37-x64\python -m pip install -r requirements.txt

csd src

REM Nuitka Compilation
C:\Python37-x64\python -m nuitka --assume-yes-for-downloads --standalone --show-progress --show-scons --user-plugin=appveyor/ttkthemes_nuitka_plugin.py --plugin-enable=tk-inter --windows-disable-console --windows-icon=icon.ico ESMB.py
mv ESMB.dist ESMB
7z a -tzip -mx9 -y ESMB-win64-nuitka.zip .\ESMB\
rd /S /Q ESMB

REM PyInstaller
C:\Python37-x64\Scripts\pyinstaller -D -y -w -i icon.ico --hidden-import ttkthemes ESMB.py
7z a -tzip -mx9 -y ESMB-win64-pyinstaller.zip .\dist\ESMB
rd /S /Q dist

C:\Python37-x64\Scripts\pyinstaller -F -y -w -i icon.ico --hidden-import ttkthemes ESMB.py
cp dist\ESMB ESMB-win64-pyinstaller.exe
rd /S /Q dist
