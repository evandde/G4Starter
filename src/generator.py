"""
Generator module for G4Starter
Handles Geant4 project generation using Cookiecutter
"""

import os
import sys
import json
import shutil
from pathlib import Path
from cookiecutter.main import cookiecutter
import questionary


def get_template_directory() -> Path:
    """
    Get cookiecutter template directory, handling PyInstaller bundling

    Returns:
        Path: Path to the cookiecutter-g4starter directory
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Running in PyInstaller bundle
        return Path(sys._MEIPASS) / 'cookiecutter-g4starter'
    else:
        # Running in normal Python
        src_dir = Path(__file__).parent
        project_root = src_dir.parent
        return project_root / 'cookiecutter-g4starter'


def cleanup_project_files(project_path: Path, context: dict):
    """
    Clean up unselected files after project generation
    This replaces the cookiecutter post_gen_project hook to ensure it works in PyInstaller

    Args:
        project_path: Path to the generated project
        context: User configuration dict
    """
    def remove_file(filepath):
        """Remove a file if it exists"""
        if filepath.exists():
            filepath.unlink()
            print(f"Removed: {filepath.name}")

    # Parse selected actions from JSON string
    selected_actions = json.loads(context.get('selected_actions', '[]'))

    # List of all possible action classes
    all_actions = ["RunAction", "EventAction", "SteppingAction", "TrackingAction", "StackingAction"]

    # Remove unselected action files
    for action in all_actions:
        if action not in selected_actions:
            header_file = project_path / "include" / f"{action}.hh"
            source_file = project_path / "src" / f"{action}.cc"
            remove_file(header_file)
            remove_file(source_file)

    # Remove PhysicsList if not using custom physics
    physics_list_type = context.get('physics_list_type', 'qbbc')
    if physics_list_type != "custom":
        physics_header = project_path / "include" / "PhysicsList.hh"
        physics_source = project_path / "src" / "PhysicsList.cc"
        remove_file(physics_header)
        remove_file(physics_source)

    # Handle SensitiveDetector files (rename or remove)
    sd_class_name = context.get('sd_class_name', '')
    placeholder_sd_header = project_path / "include" / "SensitiveDetector.hh"
    placeholder_sd_source = project_path / "src" / "SensitiveDetector.cc"

    if sd_class_name:
        # Rename placeholder to actual class name
        actual_sd_header = project_path / "include" / f"{sd_class_name}.hh"
        actual_sd_source = project_path / "src" / f"{sd_class_name}.cc"

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
    use_hit_class = context.get('use_hit_class', 'false')
    hit_class_name = context.get('hit_class_name', '')
    placeholder_hit_header = project_path / "include" / "SensitiveDetectorHit.hh"
    placeholder_hit_source = project_path / "src" / "SensitiveDetectorHit.cc"

    if use_hit_class == "true" and hit_class_name:
        actual_hit_header = project_path / "include" / f"{hit_class_name}.hh"
        actual_hit_source = project_path / "src" / f"{hit_class_name}.cc"

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
    use_custom_run = context.get('use_custom_run', 'false')
    if use_custom_run != "true":
        run_header = project_path / "include" / "Run.hh"
        run_source = project_path / "src" / "Run.cc"
        remove_file(run_header)
        remove_file(run_source)

    # Print summary
    print("\nProject generation complete!")
    if selected_actions:
        print(f"Included UserActions: {', '.join(selected_actions)}")
    else:
        print("No optional UserActions included (minimal skeleton)")

    # Display physics type
    if physics_list_type == "custom":
        physics_display = "Custom modular physics list"
    elif physics_list_type == "factory":
        factory_name = context.get('physics_factory_name', 'QBBC')
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


def generate_project(context):
    """
    Generate Geant4 project using Cookiecutter template

    Args:
        context (dict): User configuration collected from CLI

    Returns:
        Path: Path to the generated project directory, or None if cancelled
    """
    # Get the cookiecutter template directory
    template_dir = get_template_directory()

    if not template_dir.exists():
        raise FileNotFoundError(f"Template directory not found: {template_dir}")

    # Get current working directory where project will be created
    output_dir = Path.cwd()
    target_dir = output_dir / context['project_name']

    # Check if directory already exists
    if target_dir.exists():
        print(f"\n⚠️  Warning: '{context['project_name']}' folder already exists.")

        action = questionary.select(
            "How would you like to proceed?",
            choices=[
                questionary.Choice("Overwrite (delete existing folder)", value="overwrite"),
                questionary.Choice("Create with different name", value="rename"),
                questionary.Choice("Cancel", value="cancel"),
            ]
        ).ask()

        if action == "cancel" or action is None:
            print("\nProject generation cancelled.")
            return None

        elif action == "overwrite":
            confirm = questionary.confirm(
                f"Are you sure you want to delete '{context['project_name']}' folder?",
                default=False
            ).ask()

            if not confirm:
                print("\nProject generation cancelled.")
                return None

            try:
                shutil.rmtree(target_dir)
                print(f"Existing folder deleted: {target_dir}")
            except Exception as e:
                print(f"\nError: Failed to delete folder: {e}")
                return None

        elif action == "rename":
            new_name = questionary.text(
                "Enter new project name:",
                default=f"{context['project_name']}_new",
                validate=lambda text: len(text) > 0 or "Please enter a project name"
            ).ask()

            if new_name is None:
                print("\nProject generation cancelled.")
                return None

            context['project_name'] = new_name
            target_dir = output_dir / new_name

            # Check again (recursive check)
            if target_dir.exists():
                print(f"\n'{new_name}' folder also exists.")
                return generate_project(context)  # Recursive call

    # Run cookiecutter
    try:
        project_path = cookiecutter(
            str(template_dir),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir)
        )

        # Clean up unselected files (replaces post_gen_project hook)
        # This is done here instead of in hook to ensure it works in PyInstaller
        cleanup_project_files(Path(project_path), context)

        return Path(project_path)
    except Exception as e:
        print(f"\nError: Project generation failed: {e}")
        return None
