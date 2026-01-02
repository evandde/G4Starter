"""
CLI module for G4Starter
Handles all user interactions using questionary
"""

import questionary
import json


def run_cli():
    """
    Run interactive CLI and collect user inputs
    Returns a context dictionary for Cookiecutter
    """
    context = {}

    # Step 1: Project name
    print("\n[1/6] Project Information")
    project_name = questionary.text(
        "Enter project name:",
        default="MyGeant4Project",
        validate=lambda text: len(text) > 0 or "Please enter a project name"
    ).ask()

    if project_name is None:
        return None

    context['project_name'] = project_name

    # Step 2: Multithreading
    print("\n[2/6] Multithreading Configuration")
    use_mt = questionary.confirm(
        "Enable multithreading?",
        default=True
    ).ask()

    if use_mt is None:
        return None

    context['use_multithreading'] = 'true' if use_mt else 'false'

    # Step 3: Physics list
    print("\n[3/6] Physics List Configuration")
    physics_choice = questionary.select(
        "Select physics list approach:",
        choices=[
            questionary.Choice("QBBC (default reference physics list)", value="qbbc"),
            questionary.Choice("PhysicsListFactory (select from reference lists)", value="factory"),
            questionary.Choice("Custom modular physics list", value="custom"),
        ]
    ).ask()

    if physics_choice is None:
        return None

    context['physics_list_type'] = physics_choice

    # If factory, ask which reference physics list
    if physics_choice == "factory":
        factory_name = questionary.select(
            "Select reference physics list:",
            choices=[
                questionary.Choice("QBBC (general purpose, recommended)", value="QBBC"),
                questionary.Choice("FTFP_BERT (high energy physics)", value="FTFP_BERT"),
                questionary.Choice("FTFP_BERT_HP (with high precision neutrons)", value="FTFP_BERT_HP"),
                questionary.Choice("QGSP_BERT (alternative HEP)", value="QGSP_BERT"),
                questionary.Choice("QGSP_BERT_HP (with HP neutrons)", value="QGSP_BERT_HP"),
                questionary.Choice("QGSP_BIC_HP (binary cascade with HP)", value="QGSP_BIC_HP"),
                questionary.Choice("Shielding (radiation shielding)", value="Shielding"),
            ]
        ).ask()

        if factory_name is None:
            return None

        context['physics_factory_name'] = factory_name
    else:
        context['physics_factory_name'] = "QBBC"

    # Step 4: Particle source type
    print("\n[4/6] Primary Generator Configuration")
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

    # Step 5: Optional UserAction classes
    print("\n[5/6] Optional UserAction Classes")
    print("Select which UserAction classes to include (space to select, enter to continue):")
    selected_actions = questionary.checkbox(
        "Choose actions:",
        choices=[
            questionary.Choice("RunAction (BeginOfRun/EndOfRun)", value="RunAction"),
            questionary.Choice("EventAction (BeginOfEvent/EndOfEvent)", value="EventAction"),
            questionary.Choice("SteppingAction (UserSteppingAction)", value="SteppingAction"),
            questionary.Choice("TrackingAction (Pre/PostUserTrackingAction)", value="TrackingAction"),
            questionary.Choice("StackingAction (ClassifyNewTrack)", value="StackingAction"),
        ]
    ).ask()

    if selected_actions is None:
        return None

    context['selected_actions'] = json.dumps(selected_actions)

    # Step 6: Summary and confirmation
    print("\n[6/6] Confirmation")
    print("\n" + "="*60)
    print("Project Configuration Summary")
    print("="*60)
    print(f"Project name: {context['project_name']}")
    print(f"Multithreading: {'Enabled' if use_mt else 'Disabled'}")

    # Physics list display
    if physics_choice == "qbbc":
        physics_display = "QBBC (default)"
    elif physics_choice == "factory":
        physics_display = f"PhysicsListFactory - {context['physics_factory_name']}"
    else:
        physics_display = "Custom modular physics list"
    print(f"Physics list: {physics_display}")

    source_name = "G4ParticleGun" if particle_source_type == "gun" else "G4GeneralParticleSource"
    print(f"Particle source: {source_name}")

    if selected_actions:
        print(f"UserActions: {', '.join(selected_actions)}")
    else:
        print("UserActions: None (minimal skeleton)")

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
