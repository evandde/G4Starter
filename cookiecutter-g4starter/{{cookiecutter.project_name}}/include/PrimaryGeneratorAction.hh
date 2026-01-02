#ifndef PrimaryGeneratorAction_h
#define PrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"

{%- if cookiecutter.particle_source_type == "gps" %}
class G4GeneralParticleSource;
{%- else %}
class G4ParticleGun;
{%- endif %}

class PrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
public:
    PrimaryGeneratorAction();
    ~PrimaryGeneratorAction() override;

    void GeneratePrimaries(G4Event *) override;

private:
{%- if cookiecutter.particle_source_type == "gps" %}
    G4GeneralParticleSource *fPrimary;
{%- else %}
    G4ParticleGun *fPrimary;
{%- endif %}
};

#endif
