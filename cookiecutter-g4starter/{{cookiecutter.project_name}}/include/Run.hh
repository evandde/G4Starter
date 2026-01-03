{%- if cookiecutter.use_custom_run == "true" -%}
#ifndef Run_h
#define Run_h 1

#include "G4Run.hh"

class G4Event;

class Run : public G4Run
{
public:
    Run();
    ~Run() override = default;

    void RecordEvent(const G4Event* event) override;
{%- if cookiecutter.use_multithreading == "true" %}
    void Merge(const G4Run* run) override;
{%- endif %}
};

#endif
{%- endif %}
