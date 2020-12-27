@echo off
rmdir bin /s /q
pyinstaller -n ToonIslandLauncher --onefile --noupx --noconsole --icon=resources/icon.ico  --key=mwAzepLgHzCzCR2ZQ9f5QXpqRa7e9JaF5emD8BLirzy3rve7yMZ9KBqsF3wTuZWTtEvB8sLeWJfFr2TP26QxQeVp6Zo9UoCHJmqeVmsBELL5wqE4DLaQddvSNonunaZT "src/main.py"
rmdir build /s /q
REN dist bin
PAUSE