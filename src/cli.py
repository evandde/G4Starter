"""
CLI module for G4Starter
Handles all user interactions using questionary
"""

import questionary
import json


def advanced_mode(context, selected_actions):
    """
    Advanced configuration mode for Run/Hit classes
    Modifies context dict in-place
    """
    print("\n" + "="*60)
    print("Advanced Mode")
    print("="*60)
    print("Configure advanced features")
    print()

    # Build checkbox choices
    choices = [
        questionary.Choice("Custom Run class (G4Run subclass)", value="custom_run", checked=(context.get('use_custom_run') == 'true')),
    ]

    # Add Hit class option only if SensitiveDetector is defined
    sd_name = context.get('sd_class_name', '')
    if sd_name:
        choices.append(
            questionary.Choice(f"Hit class for {sd_name}", value="hit_class", checked=(context.get('use_hit_class') == 'true'))
        )

    # Show checkbox for multiple selections
    advanced_features = questionary.checkbox(
        "Select advanced features to add:",
        choices=choices
    ).ask()

    if advanced_features is None:
        return

    # Process Custom Run class
    if "custom_run" in advanced_features:
        context['use_custom_run'] = 'true'
        # If Run class requested but RunAction not selected, offer to add it
        if 'RunAction' not in selected_actions:
            add_run_action = questionary.confirm(
                "Run class requires RunAction. Add RunAction automatically?",
                default=True
            ).ask()

            if add_run_action is None:
                return

            if add_run_action:
                selected_actions.append('RunAction')
                context['selected_actions'] = json.dumps(selected_actions)
                print("  -> RunAction added to selected actions")
    else:
        context['use_custom_run'] = 'false'

    # Process Hit class
    if "hit_class" in advanced_features and sd_name:
        context['use_hit_class'] = 'true'
        # Hit class name derived from SD name
        # CalorimeterSD -> CalorimeterHit
        hit_class_name = sd_name.replace('SD', 'Hit') if sd_name.endswith('SD') else f"{sd_name}Hit"
        context['hit_class_name'] = hit_class_name
        print(f"  -> Will generate {hit_class_name} class")
    else:
        context['use_hit_class'] = 'false'
        context['hit_class_name'] = ''

    print("\nAdvanced configuration complete. Returning to confirmation...")


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

    # Step 6: SensitiveDetector (optional)
    print("\n[6/7] SensitiveDetector Class (Optional)")
    add_sd = questionary.confirm(
        "Add SensitiveDetector class?",
        default=False
    ).ask()

    if add_sd is None:
        return None

    if add_sd:
        sd_class_name = questionary.text(
            "Enter SensitiveDetector class name (e.g., CalorimeterSD, TrackerSD):",
            validate=lambda text: (
                len(text) > 0 and text.isidentifier() and text[0].isupper()
            ) or "Please enter a valid C++ class name (PascalCase, starts with uppercase)"
        ).ask()

        if sd_class_name is None:
            return None

        context['sd_class_name'] = sd_class_name
    else:
        context['sd_class_name'] = ""

    # Initialize advanced mode parameters
    context['use_custom_run'] = 'false'
    context['use_hit_class'] = 'false'
    context['hit_class_name'] = ''

    # Step 7: Confirmation with Modify option
    while True:
        # Display summary
        print("\n[7/7] Confirmation")
        print("\n" + "="*60)
        print("Project Configuration Summary")
        print("="*60)
        print(f"Project name: {context['project_name']}")
        print(f"Multithreading: {'Enabled' if use_mt else 'Disabled'}")

        # Physics display
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

        if context.get('sd_class_name'):
            print(f"SensitiveDetector: {context['sd_class_name']}")
        else:
            print("SensitiveDetector: None")

        # Display advanced mode settings if any are enabled
        if context.get('use_custom_run') == 'true':
            print("Custom Run class: Yes")
        if context.get('use_hit_class') == 'true':
            print(f"Hit class: {context.get('hit_class_name', '')}")

        print("\nNote: Configure particle properties in run.mac after generation")
        print("="*60 + "\n")

        # Three-way choice
        action = questionary.select(
            "What would you like to do?",
            choices=[
                questionary.Choice("Generate project", value="generate"),
                questionary.Choice("Modify settings (change basic options or access advanced mode)", value="modify"),
                questionary.Choice("Cancel", value="cancel"),
            ]
        ).ask()

        if action is None or action == "cancel":
            return None

        if action == "generate":
            return context

        # action == "modify"
        modify_choice = questionary.select(
            "Modify options:",
            choices=[
                questionary.Choice("Go back and change basic settings", value="restart"),
                questionary.Choice("Advanced options (Run class, Hit class, etc.)", value="advanced"),
                questionary.Choice("Return to confirmation", value="back"),
            ]
        ).ask()

        if modify_choice is None or modify_choice == "back":
            continue

        if modify_choice == "restart":
            # Show submenu to select which setting to modify
            setting_choice = questionary.select(
                "Which setting would you like to modify?",
                choices=[
                    questionary.Choice("Project name", value="project_name"),
                    questionary.Choice("Multithreading", value="multithreading"),
                    questionary.Choice("Physics list", value="physics"),
                    questionary.Choice("Particle source", value="particle_source"),
                    questionary.Choice("Optional UserActions", value="actions"),
                    questionary.Choice("SensitiveDetector", value="sd"),
                    questionary.Choice("Back to confirmation", value="back"),
                ]
            ).ask()

            if setting_choice is None or setting_choice == "back":
                continue

            # Modify selected setting
            if setting_choice == "project_name":
                new_project_name = questionary.text(
                    "Enter new project name:",
                    default=context['project_name'],
                    validate=lambda text: len(text) > 0 or "Please enter a project name"
                ).ask()
                if new_project_name is not None:
                    context['project_name'] = new_project_name
                    project_name = new_project_name

            elif setting_choice == "multithreading":
                new_use_mt = questionary.confirm(
                    "Enable multithreading?",
                    default=(context['use_multithreading'] == 'true')
                ).ask()
                if new_use_mt is not None:
                    use_mt = new_use_mt
                    context['use_multithreading'] = 'true' if new_use_mt else 'false'

            elif setting_choice == "physics":
                new_physics_choice = questionary.select(
                    "Select physics list approach:",
                    choices=[
                        questionary.Choice("QBBC (default reference physics list)", value="qbbc"),
                        questionary.Choice("PhysicsListFactory (select from reference lists)", value="factory"),
                        questionary.Choice("Custom modular physics list", value="custom"),
                    ]
                ).ask()
                if new_physics_choice is not None:
                    physics_choice = new_physics_choice
                    context['physics_list_type'] = new_physics_choice
                    if new_physics_choice == "factory":
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
                        if factory_name is not None:
                            context['physics_factory_name'] = factory_name
                    else:
                        context['physics_factory_name'] = "QBBC"

            elif setting_choice == "particle_source":
                new_particle_source_type = questionary.select(
                    "Select particle source type:",
                    choices=[
                        questionary.Choice("ParticleGun (G4ParticleGun)", value="gun"),
                        questionary.Choice("General Particle Source (G4GeneralParticleSource)", value="gps"),
                    ]
                ).ask()
                if new_particle_source_type is not None:
                    particle_source_type = new_particle_source_type
                    context['particle_source_type'] = new_particle_source_type

            elif setting_choice == "actions":
                new_selected_actions = questionary.checkbox(
                    "Choose actions:",
                    choices=[
                        questionary.Choice("RunAction (BeginOfRun/EndOfRun)", value="RunAction", checked=("RunAction" in selected_actions)),
                        questionary.Choice("EventAction (BeginOfEvent/EndOfEvent)", value="EventAction", checked=("EventAction" in selected_actions)),
                        questionary.Choice("SteppingAction (UserSteppingAction)", value="SteppingAction", checked=("SteppingAction" in selected_actions)),
                        questionary.Choice("TrackingAction (Pre/PostUserTrackingAction)", value="TrackingAction", checked=("TrackingAction" in selected_actions)),
                        questionary.Choice("StackingAction (ClassifyNewTrack)", value="StackingAction", checked=("StackingAction" in selected_actions)),
                    ]
                ).ask()
                if new_selected_actions is not None:
                    selected_actions[:] = new_selected_actions
                    context['selected_actions'] = json.dumps(selected_actions)

            elif setting_choice == "sd":
                add_sd = questionary.confirm(
                    "Add SensitiveDetector class?",
                    default=(context.get('sd_class_name', '') != '')
                ).ask()
                if add_sd is not None:
                    if add_sd:
                        sd_class_name = questionary.text(
                            "Enter SensitiveDetector class name (e.g., CalorimeterSD, TrackerSD):",
                            default=context.get('sd_class_name', ''),
                            validate=lambda text: (
                                len(text) > 0 and text.isidentifier() and text[0].isupper()
                            ) or "Please enter a valid C++ class name (PascalCase, starts with uppercase)"
                        ).ask()
                        if sd_class_name is not None:
                            context['sd_class_name'] = sd_class_name
                    else:
                        context['sd_class_name'] = ""

            continue

        if modify_choice == "advanced":
            # Call advanced mode function
            advanced_mode(context, selected_actions)
            # After advanced mode, loop back to confirmation
            continue
