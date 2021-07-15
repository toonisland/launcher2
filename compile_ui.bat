@echo off
pyrcc5 -o src/resources_rc.py qt_dev/resources.qrc
python.exe -m PyQt5.uic.pyuic .\qt_dev\launcher_interface.ui -o src/launcher_interface.py
PAUSE