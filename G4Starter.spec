# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect cookiecutter's data files and all submodules
cookiecutter_datas = collect_data_files('cookiecutter')
cookiecutter_imports = collect_submodules('cookiecutter')

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('cookiecutter-g4starter', 'cookiecutter-g4starter'),
    ] + cookiecutter_datas,
    hiddenimports=[
        'questionary',
        'questionary.prompts',
        'questionary.prompts.common',
        'questionary.prompts.select',
        'questionary.prompts.text',
        'questionary.prompts.confirm',
        'questionary.prompts.checkbox',
        'cookiecutter.main',
        'jinja2.ext',
        'prompt_toolkit',
        'prompt_toolkit.shortcuts',
        'prompt_toolkit.styles',
    ] + cookiecutter_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='G4Starter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Keep disabled for faster startup
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
