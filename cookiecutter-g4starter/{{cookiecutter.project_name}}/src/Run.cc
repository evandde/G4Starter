{%- if cookiecutter.use_custom_run == "true" -%}
#include "Run.hh"

#include "G4Event.hh"

Run::Run()
    : G4Run()
{
}

void Run::RecordEvent(const G4Event* event)
{
    G4Run::RecordEvent(event);
}

{%- if cookiecutter.use_multithreading == "true" %}

void Run::Merge(const G4Run* run)
{
    G4Run::Merge(run);
}
{%- endif %}
{%- endif %}
