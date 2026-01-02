"""
Generator module for G4Starter
Handles Geant4 project generation using Cookiecutter
"""

import os
import shutil
from pathlib import Path
from cookiecutter.main import cookiecutter
import questionary


def generate_project(context):
    """
    Generate Geant4 project using Cookiecutter template

    Args:
        context (dict): User configuration collected from CLI

    Returns:
        Path: Path to the generated project directory, or None if cancelled
    """
    # Get the cookiecutter template directory
    src_dir = Path(__file__).parent
    project_root = src_dir.parent
    template_dir = project_root / 'cookiecutter-g4starter'

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
                print(f"✅ Existing folder deleted: {target_dir}")
            except Exception as e:
                print(f"\n❌ Error: Failed to delete folder: {e}")
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
                print(f"\n⚠️  '{new_name}' folder also exists.")
                return generate_project(context)  # Recursive call

    # Run cookiecutter
    try:
        project_path = cookiecutter(
            str(template_dir),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir)
        )
        return Path(project_path)
    except Exception as e:
        print(f"\n❌ Error: Project generation failed: {e}")
        return None
