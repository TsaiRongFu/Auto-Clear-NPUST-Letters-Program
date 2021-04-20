# -*- mode: python ; coding: utf-8 -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='82d96a60e60bfb64d042e02e5e7e0e7361ae8a79f78954d5707ab68ba2641544686038d2b1e20ea2740b4663dd91672158d742c9b4c790268c8c82fcd8bf7848')


a = Analysis(['Auto-Clean-NPUST-Mail-Program.py'],
             pathex=['C:\\Users\\RONGF\\Desktop\\PythonTestExe'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='Auto-Clean-NPUST-Mail-Program',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='code-programming-signs.ico')
