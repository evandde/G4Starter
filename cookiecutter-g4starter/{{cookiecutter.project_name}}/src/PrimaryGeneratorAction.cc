#include "PrimaryGeneratorAction.hh"

PrimaryGeneratorAction::PrimaryGeneratorAction()
    : G4VUserPrimaryGeneratorAction()
{
{%- if cookiecutter.particle_source_type == "gps" %}
    fPrimary = new G4GeneralParticleSource();
{%- else %}
    fPrimary = new G4ParticleGun();
{%- endif %}
}

PrimaryGeneratorAction::~PrimaryGeneratorAction()
{
    delete fPrimary;
}

void PrimaryGeneratorAction::GeneratePrimaries(G4Event *event)
{
    fPrimary->GeneratePrimaryVertex(event);
}
