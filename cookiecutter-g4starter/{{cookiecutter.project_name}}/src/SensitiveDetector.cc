{%- if cookiecutter.sd_class_name -%}
#include "{{ cookiecutter.sd_class_name }}.hh"

#include "G4HCofThisEvent.hh"
#include "G4Step.hh"

{{ cookiecutter.sd_class_name }}::{{ cookiecutter.sd_class_name }}(const G4String& name)
    : G4VSensitiveDetector(name)
{
}

{{ cookiecutter.sd_class_name }}::~{{ cookiecutter.sd_class_name }}()
{
}

void {{ cookiecutter.sd_class_name }}::Initialize(G4HCofThisEvent*)
{
}

G4bool {{ cookiecutter.sd_class_name }}::ProcessHits(G4Step* step, G4TouchableHistory*)
{
    return true;
}

void {{ cookiecutter.sd_class_name }}::EndOfEvent(G4HCofThisEvent*)
{
}
{%- endif %}
