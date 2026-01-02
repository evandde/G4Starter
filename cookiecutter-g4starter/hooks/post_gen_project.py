#!/usr/bin/env python
"""
Post-generation hook for G4Starter
Removes unselected UserAction files and PhysicsList if not using custom physics
"""

import os
import json
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


if __name__ == "__main__":
    main()
