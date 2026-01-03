#!/usr/bin/env python3
"""
G4Starter - Geant4 Project Generator
Interactive CLI tool for generating Geant4 simulation projects
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_dir = Path(__file__).parent
sys.path.insert(0, str(src_dir))

from cli import run_cli
from generator import generate_project


def get_build_instructions(project_name: str) -> list[str]:
    """Generate OS-specific build instructions"""
    if sys.platform == 'win32':
        return [
            f"cd {project_name}",
            "mkdir build",
            "cd build",
            "cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release",
            "ninja",
            f".\\{project_name}.exe"
        ]
    else:  # Linux, macOS
        return [
            f"cd {project_name}",
            "mkdir build && cd build",
            "cmake .. -DCMAKE_BUILD_TYPE=Release",
            "make",
            f"./{project_name}"
        ]


def main():
    """Main entry point for G4Starter"""
    import os

    # Prevent re-execution by cookiecutter subprocess
    # Cookiecutter may spawn a new Python process, which would re-run main()
    if os.environ.get('G4STARTER_RUNNING') == '1':
        # We're in a subprocess spawned by cookiecutter, exit silently
        return 0

    # Mark that we're running
    os.environ['G4STARTER_RUNNING'] = '1'

    print("="*60)
    print("  G4Starter - Geant4 Project Generator")
    print("="*60)
    print()

    try:
        # Run interactive CLI to collect user inputs
        context = run_cli()

        if context is None:
            print("\nProject generation cancelled.")
            return 0

        # Generate Geant4 project using collected context
        print("\nGenerating project...")
        project_path = generate_project(context)

        # Check if project generation was successful
        if project_path is None:
            # User cancelled or error occurred (message already printed)
            return 1

        print("\n" + "="*60)
        print(f"Geant4 project successfully generated!")
        print(f"Project location: {project_path}")
        print("="*60)
        print("\nNext steps:")
        for instruction in get_build_instructions(context['project_name']):
            print(f"  {instruction}")
        print()

        return 0

    except KeyboardInterrupt:
        print("\n\nProject generation interrupted.")
        return 1
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
