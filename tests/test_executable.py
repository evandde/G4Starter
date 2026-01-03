#!/usr/bin/env python3
"""
Smoke test for G4Starter executable
Tests bundled executable, not source code
"""
import subprocess
import sys
import time
from pathlib import Path


def test_executable_exists():
    """Test that executable exists"""
    exe_name = 'G4Starter.exe' if sys.platform == 'win32' else 'G4Starter'
    exe_path = Path('dist') / exe_name

    if not exe_path.exists():
        print(f"[FAIL] Executable not found at {exe_path}")
        return False

    print(f"[PASS] Executable exists at {exe_path}")
    return True


def test_executable_runs():
    """Test that executable starts"""
    exe_name = 'G4Starter.exe' if sys.platform == 'win32' else './G4Starter'
    exe_path = Path('dist') / exe_name

    try:
        # Run with timeout, send interrupt
        process = subprocess.Popen(
            [str(exe_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(2)  # Let it start
        process.terminate()  # Send SIGTERM
        stdout, stderr = process.communicate(timeout=5)

        if "G4Starter" in stdout:
            print("[PASS] Executable runs and displays banner")
            return True
        else:
            print("[FAIL] Unexpected output")
            print(stdout)
            return False

    except Exception as e:
        print(f"[FAIL] {e}")
        return False


if __name__ == '__main__':
    print("Running smoke tests for G4Starter executable\n")

    tests = [
        test_executable_exists,
        test_executable_runs,
    ]

    passed = sum(test() for test in tests)
    total = len(tests)

    print(f"\n{passed}/{total} tests passed")
    sys.exit(0 if passed == total else 1)
