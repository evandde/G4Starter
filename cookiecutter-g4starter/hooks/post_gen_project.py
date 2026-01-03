#!/usr/bin/env python
"""
Post-generation hook for G4Starter
Removes unselected UserAction files, PhysicsList, and renames/removes SD/Hit/Run files
"""

import os
import json
import shutil
from pathlib import Path


def remove_file(filepath):
    """Remove a file if it exists"""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed: {filepath}")


def main():
    """Main hook function"""
    project_root = Path.cwd()

    # Parse selected actions from JSON string
    selected_actions_json = """{{ cookiecutter.selected_actions }}"""
    selected_actions = json.loads(selected_actions_json)

    # List of all possible action classes
    all_actions = ["RunAction", "EventAction", "SteppingAction", "TrackingAction", "StackingAction"]

    # Remove unselected action files
    for action in all_actions:
        if action not in selected_actions:
            header_file = project_root / "include" / f"{action}.hh"
            source_file = project_root / "src" / f"{action}.cc"
            remove_file(header_file)
            remove_file(source_file)

    # Remove PhysicsList if not using custom physics
    physics_list_type = "{{ cookiecutter.physics_list_type }}"
    if physics_list_type != "custom":
        physics_header = project_root / "include" / "PhysicsList.hh"
        physics_source = project_root / "src" / "PhysicsList.cc"
        remove_file(physics_header)
        remove_file(physics_source)

    # Handle SensitiveDetector files (rename or remove)
    sd_class_name = """{{ cookiecutter.sd_class_name }}"""
    placeholder_sd_header = project_root / "include" / "SensitiveDetector.hh"
    placeholder_sd_source = project_root / "src" / "SensitiveDetector.cc"

    if sd_class_name:
        # Rename placeholder to actual class name
        actual_sd_header = project_root / "include" / f"{sd_class_name}.hh"
        actual_sd_source = project_root / "src" / f"{sd_class_name}.cc"

        if placeholder_sd_header.exists():
            shutil.move(str(placeholder_sd_header), str(actual_sd_header))
            print(f"Renamed: SensitiveDetector.hh -> {sd_class_name}.hh")
        if placeholder_sd_source.exists():
            shutil.move(str(placeholder_sd_source), str(actual_sd_source))
            print(f"Renamed: SensitiveDetector.cc -> {sd_class_name}.cc")
    else:
        # Remove placeholder files
        remove_file(placeholder_sd_header)
        remove_file(placeholder_sd_source)

    # Handle Hit class files (rename or remove)
    use_hit_class = "{{ cookiecutter.use_hit_class }}"
    hit_class_name = """{{ cookiecutter.hit_class_name }}"""
    placeholder_hit_header = project_root / "include" / "SensitiveDetectorHit.hh"
    placeholder_hit_source = project_root / "src" / "SensitiveDetectorHit.cc"

    if use_hit_class == "true" and hit_class_name:
        actual_hit_header = project_root / "include" / f"{hit_class_name}.hh"
        actual_hit_source = project_root / "src" / f"{hit_class_name}.cc"

        if placeholder_hit_header.exists():
            shutil.move(str(placeholder_hit_header), str(actual_hit_header))
            print(f"Renamed: SensitiveDetectorHit.hh -> {hit_class_name}.hh")
        if placeholder_hit_source.exists():
            shutil.move(str(placeholder_hit_source), str(actual_hit_source))
            print(f"Renamed: SensitiveDetectorHit.cc -> {hit_class_name}.cc")
    else:
        remove_file(placeholder_hit_header)
        remove_file(placeholder_hit_source)

    # Handle Run class files
    use_custom_run = "{{ cookiecutter.use_custom_run }}"
    if use_custom_run != "true":
        run_header = project_root / "include" / "Run.hh"
        run_source = project_root / "src" / "Run.cc"
        remove_file(run_header)
        remove_file(run_source)

    # Final summary
    print("\nProject generation complete!")
    if selected_actions:
        print(f"Included UserActions: {', '.join(selected_actions)}")
    else:
        print("No optional UserActions included (minimal skeleton)")

    # Display physics type
    if physics_list_type == "custom":
        physics_display = "Custom modular physics list"
    elif physics_list_type == "factory":
        factory_name = "{{ cookiecutter.physics_factory_name }}"
        physics_display = f"PhysicsListFactory - {factory_name}"
    else:
        physics_display = "QBBC"
    print(f"Physics list: {physics_display}")

    # Display SD/Hit/Run status
    if sd_class_name:
        print(f"SensitiveDetector: {sd_class_name}")
    if use_hit_class == "true" and hit_class_name:
        print(f"Hit class: {hit_class_name}")
    if use_custom_run == "true":
        print("Custom Run class: Yes")


if __name__ == "__main__":
    main()
