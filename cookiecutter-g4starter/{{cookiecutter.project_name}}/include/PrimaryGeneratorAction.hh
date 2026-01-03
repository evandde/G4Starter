#ifndef PrimaryGeneratorAction_h
#define PrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"
{%- if cookiecutter.particle_source_type == "gps" %}
#include "G4GeneralParticleSource.hh"
{%- else %}
#include "G4ParticleGun.hh"
{%- endif %}

class PrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
public:
    PrimaryGeneratorAction();
    ~PrimaryGeneratorAction() override;

    void GeneratePrimaries(G4Event *event) override;

private:
{%- if cookiecutter.particle_source_type == "gps" %}
    G4GeneralParticleSource *fPrimary;
{%- else %}
    G4ParticleGun *fPrimary;
{%- endif %}
};

#endif
