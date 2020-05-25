# On MacOS, this is the only way i found to get a python with tcl 8.6+.
wget https://www.python.org/ftp/python/3.7.6/python-3.7.6-macosx10.9.pkg -O python3.pkg
sudo installer -pkg python3.pkg -target /

# Setup required python packages
python3.7 -m pip install setuptools wheel
python3.7 -m pip install PyInstaller
python3.7 -m pip install -r requirements.txt

# Build a directory distribution ("-D") with PyInstaller
# We have to add the data folder here since it won't be added automatically. See utils/loadtooltips.py for an example of how to access it
python3.7 -m PyInstaller -D --noconfirm --hidden-import ttkthemes --add-data "src/data:data" --windowed src/ESMB.py
# Archive with maximum zip compression
env GZIP=-9 tar -czf ./ESMB-macos10.15-pyinstaller.tar.gz dist/ESMB/
env GZIP=-9 tar -czf ./ESMB-macos10.15-pyinstaller-app.tar.gz dist/ESMB.app
# Cleanup
rm -rf dist/

# Build a OneFile executable ("-F") with PyInstaller
# We have to add the data folder here since it won't be added automatically. See utils/loadtooltips.py for an example of how to access it
python3.7 -m PyInstaller -F --noconfirm --hidden-import ttkthemes --add-data "src/data:data" src/ESMB.py
cp dist/ESMB ESMB-ubuntu-macos10.15-pyinstaller
# Cleanup
rm -rf dist/
