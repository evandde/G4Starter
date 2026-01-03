#include "RunAction.hh"
{%- if cookiecutter.use_custom_run == "true" %}
#include "Run.hh"
{%- endif %}

#include "G4RunManager.hh"
{%- if cookiecutter.use_custom_run == "true" %}

G4Run* RunAction::GenerateRun()
{
    return new Run;
}
{%- endif %}

void RunAction::BeginOfRunAction(const G4Run* run)
{
}

void RunAction::EndOfRunAction(const G4Run* run)
{
}
