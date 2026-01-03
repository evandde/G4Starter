#!/usr/bin/env python3
"""
Build script for G4Starter
Creates standalone executable using PyInstaller
"""
import sys
import shutil
from pathlib import Path
import subprocess


def clean_build():
    """Remove previous build artifacts"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        path = Path(dir_name)
        if path.exists():
            print(f"Cleaning {dir_name}...")
            shutil.rmtree(path)


def build_executable():
    """Build using PyInstaller"""
    print("Building G4Starter executable...")
    result = subprocess.run(
        [sys.executable, '-m', 'PyInstaller', 'G4Starter.spec'],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Build failed!")
        print(result.stderr)
        return False

    print("Build successful!")
    return True


def verify_build():
    """Verify executable was created"""
    exe_name = 'G4Starter.exe' if sys.platform == 'win32' else 'G4Starter'
    exe_path = Path('dist') / exe_name

    if not exe_path.exists():
        print(f"Error: {exe_path} not found!")
        return False

    size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"\nExecutable: {exe_path}")
    print(f"Size: {size_mb:.2f} MB")

    return True


if __name__ == '__main__':
    clean_build()
    if build_executable() and verify_build():
        print("\n[SUCCESS] Build complete! Executable is in dist/")
        sys.exit(0)
    else:
        print("\n[FAILED] Build failed!")
        sys.exit(1)
