#include "ActionInitialization.hh"
#include "PrimaryGeneratorAction.hh"
{%- if '"RunAction"' in cookiecutter.selected_actions %}
#include "RunAction.hh"
{%- endif %}
{%- if '"EventAction"' in cookiecutter.selected_actions %}
#include "EventAction.hh"
{%- endif %}
{%- if '"SteppingAction"' in cookiecutter.selected_actions %}
#include "SteppingAction.hh"
{%- endif %}
{%- if '"TrackingAction"' in cookiecutter.selected_actions %}
#include "TrackingAction.hh"
{%- endif %}
{%- if '"StackingAction"' in cookiecutter.selected_actions %}
#include "StackingAction.hh"
{%- endif %}

{%- if cookiecutter.use_multithreading == "true" %}
void ActionInitialization::BuildForMaster() const
{
{%- if '"RunAction"' in cookiecutter.selected_actions %}
    SetUserAction(new RunAction);
{%- endif %}
}
{%- endif %}

void ActionInitialization::Build() const
{
    SetUserAction(new PrimaryGeneratorAction);
{%- if '"RunAction"' in cookiecutter.selected_actions %}
    SetUserAction(new RunAction);
{%- endif %}
{%- if '"EventAction"' in cookiecutter.selected_actions %}
    SetUserAction(new EventAction);
{%- endif %}
{%- if '"SteppingAction"' in cookiecutter.selected_actions %}
    SetUserAction(new SteppingAction);
{%- endif %}
{%- if '"TrackingAction"' in cookiecutter.selected_actions %}
    SetUserAction(new TrackingAction);
{%- endif %}
{%- if '"StackingAction"' in cookiecutter.selected_actions %}
    SetUserAction(new StackingAction);
{%- endif %}
}
