# -*- mode: python -*-

block_cipher = None
import pkg_resources

a = Analysis(['main_app.py'],
             pathex=['F:\\BATCODERS\\Desktop\\TBAT\\tbat_v4'],
             binaries=[],
             datas=[(
                pkg_resources.resource_filename('arabic_reshaper', 'default-config.ini'),
                'arabic_reshaper'
            ),],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='TBAT V4',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
