# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

import PyQt6


# PyQt6 wheels can ship a newer MSVC runtime than the Python distribution.
# Put that runtime beside the executable so Windows does not load an older,
# ABI-incompatible copy collected from Python first.
qt_bin = Path(PyQt6.__file__).resolve().parent / 'Qt6' / 'bin'
msvc_runtime = [
    (str(path), '.')
    for pattern in ('MSVCP140*.dll', 'VCRUNTIME140*.dll')
    for path in qt_bin.glob(pattern)
]

analysis = Analysis(
    ['scripts/flameTracker.py'],
    pathex=['scripts'],
    binaries=msvc_runtime,
    datas=[('VERSION', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Qt on Windows uses the operating-system ICU shim. A third-party ICU found on
# PATH (for example, from PDF tooling) is ABI-incompatible and must not be
# bundled as Qt6Core's unversioned icuuc.dll dependency.
analysis.binaries = [
    entry
    for entry in analysis.binaries
    if Path(entry[0]).name.lower() != 'icuuc.dll'
    and not Path(entry[0]).name.lower().startswith('icudt')
]
pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    [],
    name='flameTracker-windows-x64',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
