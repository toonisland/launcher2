# -*- mode: python ; coding: utf-8 -*-


block_cipher = pyi_crypto.PyiBlockCipher(key='mwAzepLgHzCzCR2ZQ9f5QXpqRa7e9JaF5emD8BLirzy3rve7yMZ9KBqsF3wTuZWTtEvB8sLeWJfFr2TP26QxQeVp6Zo9UoCHJmqeVmsBELL5wqE4DLaQddvSNonunaZT')


a = Analysis(['src\\main.py'],
             pathex=['C:\\Users\\Nora\\TIA\\launcher2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='ToonIslandLauncher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='resources\\icon.ico')
