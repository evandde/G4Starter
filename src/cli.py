"""
CLI module for G4Starter
Handles all user interactions using questionary
"""

import questionary


def run_cli():
    """
    Run interactive CLI and collect user inputs
    Returns a context dictionary for Cookiecutter
    """
    context = {}

    # Step 1: Project name
    print("\n[1/3] Project Information")
    project_name = questionary.text(
        "Enter project name:",
        default="MyGeant4Project",
        validate=lambda text: len(text) > 0 or "Please enter a project name"
    ).ask()

    if project_name is None:
        return None

    context['project_name'] = project_name

    # Step 2: Particle source type
    print("\n[2/3] Primary Generator Configuration")
    particle_source_type = questionary.select(
        "Select particle source type:",
        choices=[
            questionary.Choice("ParticleGun (G4ParticleGun)", value="gun"),
            questionary.Choice("General Particle Source (G4GeneralParticleSource)", value="gps"),
        ]
    ).ask()

    if particle_source_type is None:
        return None

    context['particle_source_type'] = particle_source_type

    # Step 3: Multithreading
    print("\n[3/3] Multithreading Configuration")
    use_mt = questionary.confirm(
        "Enable multithreading?",
        default=True
    ).ask()

    if use_mt is None:
        return None

    context['use_multithreading'] = 'true' if use_mt else 'false'

    # Summary
    print("\n" + "="*60)
    print("Project Configuration Summary")
    print("="*60)
    print(f"Project name: {context['project_name']}")
    source_name = "G4ParticleGun" if particle_source_type == "gun" else "G4GeneralParticleSource"
    print(f"Particle source: {source_name}")
    print(f"Multithreading: {'Enabled' if use_mt else 'Disabled'}")
    print("\nNote: Configure particle properties in run.mac after generation")
    print("="*60 + "\n")

    # Confirm
    confirm = questionary.confirm(
        "Generate project with these settings?",
        default=True
    ).ask()

    if not confirm:
        return None

    return context
