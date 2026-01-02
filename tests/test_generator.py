#!/usr/bin/env python3
"""
G4Starter test script
Automatically performs project generation and basic validation.
"""

import sys
import os
import shutil
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent.parent
src_dir = project_root / 'src'
sys.path.insert(0, str(src_dir))

from generator import generate_project


def test_project_generation():
    """Test project generation"""
    print("="*60)
    print("  G4Starter Automated Test")
    print("="*60)
    print()

    # Define test context
    test_context = {
        'project_name': 'TestG4Project',
        'particle_source_type': 'gps',
        'use_multithreading': 'true'
    }

    print("📝 Test configuration:")
    print(f"  - Project name: {test_context['project_name']}")
    print(f"  - Source type: {test_context['particle_source_type']}")
    print(f"  - Multithreading: {test_context['use_multithreading']}")
    print()

    # Delete existing test project
    test_dir = Path.cwd() / test_context['project_name']
    if test_dir.exists():
        print(f"🗑️  Deleting existing test project: {test_dir}")
        shutil.rmtree(test_dir)

    # Generate project
    print("\n🔨 Generating project...")
    project_path = generate_project(test_context)

    if project_path is None:
        print("\n❌ Test failed: Project generation failed")
        return False

    print(f"\n✅ Project generation complete: {project_path}")

    # Validate generated files
    print("\n📂 Validating file structure:")
    required_files = [
        'CMakeLists.txt',
        'main.cc',
        'vis.mac',
        'run.mac',
        'include/DetectorConstruction.hh',
        'include/ActionInitialization.hh',
        'include/PrimaryGeneratorAction.hh',
        'src/DetectorConstruction.cc',
        'src/ActionInitialization.cc',
        'src/PrimaryGeneratorAction.cc',
    ]

    all_exist = True
    for file_path in required_files:
        full_path = project_path / file_path
        exists = full_path.exists()
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if not exists:
            all_exist = False

    # Validate run.mac content
    print("\n📄 Validating run.mac content:")
    run_mac = project_path / 'run.mac'
    if run_mac.exists():
        content = run_mac.read_text()
        checks = [
            ('/run/beamOn 100' in content, 'Run beam command'),
            ('/control/verbose' in content, 'Verbosity settings'),
        ]

        for expected, description in checks:
            status = "✅" if expected else "❌"
            print(f"  {status} {description}")
            if not expected:
                all_exist = False
    else:
        print("  ❌ run.mac file does not exist")
        all_exist = False

    # Validate PrimaryGeneratorAction (check GPS usage)
    print("\n🔬 Validating PrimaryGeneratorAction (GPS):")
    pga_header = project_path / 'include' / 'PrimaryGeneratorAction.hh'
    pga_source = project_path / 'src' / 'PrimaryGeneratorAction.cc'

    if pga_header.exists() and pga_source.exists():
        header_content = pga_header.read_text()
        source_content = pga_source.read_text()

        gps_checks = [
            ('G4GeneralParticleSource' in header_content, 'Header: G4GeneralParticleSource declaration'),
            ('G4GeneralParticleSource.hh' in source_content, 'Source: G4GeneralParticleSource header inclusion'),
            ('new G4GeneralParticleSource()' in source_content, 'Source: GPS object creation'),
        ]

        for check, description in gps_checks:
            status = "✅" if check else "❌"
            print(f"  {status} {description}")
            if not check:
                all_exist = False
    else:
        print("  ❌ PrimaryGeneratorAction files do not exist")
        all_exist = False

    print("\n" + "="*60)
    if all_exist:
        print("✅ All tests passed!")
        print(f"\nGenerated project: {project_path}")
        print("\nNext steps (if Geant4 is installed):")
        print(f"  cd {test_context['project_name']}")
        print("  mkdir build && cd build")
        print("  cmake ..")
        print("  cmake --build .")
    else:
        print("❌ Some tests failed")
        return False
    print("="*60)

    return True


if __name__ == "__main__":
    try:
        success = test_project_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
