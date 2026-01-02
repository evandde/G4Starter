#!/usr/bin/env python3
"""
G4Starter test script
Automatically performs project generation and basic validation.
"""

import sys
import os
import shutil
import json
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent.parent
src_dir = project_root / 'src'
sys.path.insert(0, str(src_dir))

from generator import generate_project


def test_project_generation():
    """Test project generation"""
    print("="*60)
    print("  G4Starter Automated Test - Phase 2")
    print("="*60)
    print()

    # Define test context (Phase 2 with restructured CLI)
    test_context = {
        'project_name': 'TestG4Project',
        'use_multithreading': 'true',
        'physics_list_type': 'qbbc',
        'physics_factory_name': 'QBBC',
        'particle_source_type': 'gps',
        'selected_actions': json.dumps(['RunAction', 'EventAction'])
    }

    print("Test configuration:")
    print(f"  - Project name: {test_context['project_name']}")
    print(f"  - Multithreading: {test_context['use_multithreading']}")
    print(f"  - Physics type: {test_context['physics_list_type']}")
    print(f"  - Source type: {test_context['particle_source_type']}")
    print(f"  - Selected actions: {test_context['selected_actions']}")
    print()

    # Delete existing test project
    test_dir = Path.cwd() / test_context['project_name']
    if test_dir.exists():
        print(f"Deleting existing test project: {test_dir}")
        shutil.rmtree(test_dir)

    # Generate project
    print("\nGenerating project...")
    project_path = generate_project(test_context)

    if project_path is None:
        print("\nTest failed: Project generation failed")
        return False

    print(f"\nProject generation complete: {project_path}")

    # Validate generated files
    print("\nValidating file structure:")
    required_files = [
        'CMakeLists.txt',
        'main.cc',
        'vis.mac',
        'run.mac',
        'include/DetectorConstruction.hh',
        'include/ActionInitialization.hh',
        'include/PrimaryGeneratorAction.hh',
        'include/RunAction.hh',
        'include/EventAction.hh',
        'src/DetectorConstruction.cc',
        'src/ActionInitialization.cc',
        'src/PrimaryGeneratorAction.cc',
        'src/RunAction.cc',
        'src/EventAction.cc',
    ]

    # Files that should NOT exist based on test context
    should_not_exist = [
        'include/SteppingAction.hh',
        'include/TrackingAction.hh',
        'include/StackingAction.hh',
        'include/PhysicsList.hh',
        'src/SteppingAction.cc',
        'src/TrackingAction.cc',
        'src/StackingAction.cc',
        'src/PhysicsList.cc',
    ]

    all_exist = True
    for file_path in required_files:
        full_path = project_path / file_path
        exists = full_path.exists()
        status = "+" if exists else "-"
        print(f"  {status} {file_path}")
        if not exists:
            all_exist = False

    print("\nValidating excluded files (should not exist):")
    for file_path in should_not_exist:
        full_path = project_path / file_path
        exists = full_path.exists()
        status = "-" if not exists else "+"
        print(f"  {status} {file_path} {'(correctly excluded)' if not exists else '(ERROR: should not exist)'}")
        if exists:
            all_exist = False

    # Validate run.mac content
    print("\nValidating run.mac content:")
    run_mac = project_path / 'run.mac'
    if run_mac.exists():
        content = run_mac.read_text()
        checks = [
            ('/run/beamOn 100' in content, 'Run beam command'),
            ('/control/verbose' in content, 'Verbosity settings'),
        ]

        for expected, description in checks:
            status = "+" if expected else "-"
            print(f"  {status} {description}")
            if not expected:
                all_exist = False
    else:
        print("  - run.mac file does not exist")
        all_exist = False

    # Validate PrimaryGeneratorAction (check GPS usage)
    print("\nValidating PrimaryGeneratorAction (GPS):")
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
            status = "+" if check else "-"
            print(f"  {status} {description}")
            if not check:
                all_exist = False
    else:
        print("  - PrimaryGeneratorAction files do not exist")
        all_exist = False

    # Validate ActionInitialization (check conditional registration)
    print("\nValidating ActionInitialization (conditional actions):")
    action_init_source = project_path / 'src' / 'ActionInitialization.cc'
    if action_init_source.exists():
        content = action_init_source.read_text()
        action_checks = [
            ('new RunAction' in content, 'RunAction registration'),
            ('new EventAction' in content, 'EventAction registration'),
            ('new SteppingAction' not in content, 'SteppingAction not registered (correct)'),
        ]

        for check, description in action_checks:
            status = "+" if check else "-"
            print(f"  {status} {description}")
            if not check:
                all_exist = False
    else:
        print("  - ActionInitialization.cc does not exist")
        all_exist = False

    # Validate main.cc (check QBBC usage, not custom physics)
    print("\nValidating main.cc (QBBC physics):")
    main_cc = project_path / 'main.cc'
    if main_cc.exists():
        content = main_cc.read_text()
        physics_checks = [
            ('#include "QBBC.hh"' in content, 'QBBC header included'),
            ('new QBBC' in content, 'QBBC instantiation'),
            ('#include "PhysicsList.hh"' not in content, 'PhysicsList not included (correct)'),
        ]

        for check, description in physics_checks:
            status = "+" if check else "-"
            print(f"  {status} {description}")
            if not check:
                all_exist = False
    else:
        print("  - main.cc does not exist")
        all_exist = False

    print("\n" + "="*60)
    if all_exist:
        print("All tests passed!")
        print(f"\nGenerated project: {project_path}")
        print("\nNext steps (if Geant4 is installed):")
        print(f"  cd {test_context['project_name']}")
        print("  mkdir build && cd build")
        print("  cmake ..")
        print("  cmake --build .")
    else:
        print("Some tests failed")
        return False
    print("="*60)

    return True


if __name__ == "__main__":
    try:
        success = test_project_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
