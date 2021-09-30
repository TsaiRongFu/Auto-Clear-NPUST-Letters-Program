# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Auto-Clean-NPUST-Mail-Program-Edge.py'],
             pathex=['C:\\Users\\Eggs\\Desktop\\github project\\Auto-Clear-NPUST-Letters-Program'],
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
          name='Auto-Clean-NPUST-Mail-Program-Edge',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='Auto-Clean-NPUST-Mail-Program.ico')
