# Setup
# chrpath can be required for nuitka's scons command, to adjust shared library paths
sudo apt-get update && sudo apt-get -y install python3-pip python3-tk chrpath
pip3 install nuitka PyInstaller
pip3 install -r requirements.txt

# move into the folder containing ESMB.py
cd src

# Nuitka Compilation
python3 -m nuitka --assume-yes-for-downloads --standalone --show-progress --show-scons --user-plugin=../appveyor/ttkthemes_nuitka_plugin.py ESMB.py
mv ESMB.dist ESMB
tar -czvf ESMB-ubuntu-amd64-nuitka.tar.gz ESMB/
rm -rf ESMB

# PyInstaller
python3 -m pyinstaller -D -y -w --hidden-import ttkthemes ESMB.py
tar -czvf ESMB-ubuntu-amd64-pyinstaller.tar.gz dist/ESMB/
rm -rf dist

python3 -m pyinstaller -F -y -w --hidden-import ttkthemes ESMB.py
cp dist/ESMB ESMB-ubuntu-amd64-pyinstaller
rm -rf dist
