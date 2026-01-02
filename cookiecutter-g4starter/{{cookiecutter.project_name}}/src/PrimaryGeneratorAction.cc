#include "PrimaryGeneratorAction.hh"

{%- if cookiecutter.particle_source_type == "gps" %}
#include "G4GeneralParticleSource.hh"

PrimaryGeneratorAction::PrimaryGeneratorAction()
    : G4VUserPrimaryGeneratorAction()
{
    fPrimary = new G4GeneralParticleSource();
}
{%- else %}
#include "G4ParticleGun.hh"

PrimaryGeneratorAction::PrimaryGeneratorAction()
    : G4VUserPrimaryGeneratorAction()
{
    fPrimary = new G4ParticleGun();
}
{%- endif %}

PrimaryGeneratorAction::~PrimaryGeneratorAction()
{
    delete fPrimary;
}

void PrimaryGeneratorAction::GeneratePrimaries(G4Event *anEvent)
{
    fPrimary->GeneratePrimaryVertex(anEvent);
}
