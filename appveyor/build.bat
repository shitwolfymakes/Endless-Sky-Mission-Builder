REM Setup
C:\Python37-x64\python -m pip install nuitka pyinstaller

REM Nuitka Compilation
C:\Python37-x64\python -m nuitka --assume-yes-for-downloads --standalone --show-progress --show-scons --plugin-enable=tk-inter ESMB.py
mv ESMB.dist ESMB
7z a -tzip -mx9 -y ESMB-win64-nuitka.zip .\ESMB\
rd /S /Q ESMB

REM PyInstaller
C:\Python37-x64\Scripts\pyinstaller -D -y -w ESMB.py
7z a -tzip -mx9 -y ESMB-win64-pyinstaller.zip .\dist\ESMB
rd /S /Q dist

C:\Python37-x64\Scripts\pyinstaller -F -y -w ESMB.py
cp dist\ESMB ESMB-win64-pyinstaller.exe
rd /S /Q dist
