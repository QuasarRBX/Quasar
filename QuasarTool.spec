# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_quasar.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pyisemail', 'pyisemail.diagnosis', 'pyisemail.validators', 'pystyle', 'termcolor', 'tqdm', 'rich', 'rich.console', 'rich.text', 'rich.style', 'rich.highlighter', 'rich.pretty', 'rich.traceback', 'requests', 'queue', 'webbrowser', 'glob', 're', 'socket', 'threading', 'json', 'time', 'os', 'sys', 'string', 'subprocess', 'random', 'ctypes', 'ctypes.wintypes'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QuasarTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\user\\Pictures\\quASA\\icon.ico'],
)
