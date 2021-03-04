# Install pip, python3-tk (tkinter package), python3.7 and python3.7-dev (to have libraries available)
# Python HAS to be version 3.7+, otherwise PyInstaller binaries will have import errors for some reason
sudo apt-get update && sudo apt-get -y install python3-pip python3-tk python3.7 python3.7-dev

# Setup required python packages
python3.7 -m pip install PyInstaller
python3.7 -m pip install -r requirements.txt

# Build a directory distribution ("-D") with PyInstaller
# We have to add the data folder here since it won't be added automatically. See utils/loadtooltips.py for an example of how to access it
python3.7 -m PyInstaller -D --noconfirm --path src --hidden-import ttkthemes --add-data "src/data:data" src/ESMB.py
# Archive with maximum zip compression
env GZIP=-9 tar -czf ./ESMB-ubuntu-amd64-pyinstaller.tar.gz dist/ESMB/
# Cleanup
rm -rf dist/

# Build a OneFile executable ("-F") with PyInstaller
# We have to add the data folder here since it won't be added automatically. See utils/loadtooltips.py for an example of how to access it
python3.7 -m PyInstaller -F --noconfirm --path src --hidden-import ttkthemes --add-data "src/data:data" src/ESMB.py
cp dist/ESMB ESMB-ubuntu-amd64-pyinstaller
# Cleanup
rm -rf dist/