#ifndef ActionInitialization_h
#define ActionInitialization_h 1

#include "G4VUserActionInitialization.hh"

class ActionInitialization : public G4VUserActionInitialization
{
public:
    ActionInitialization() = default;
    ~ActionInitialization() override = default;

{%- if cookiecutter.use_multithreading == "true" %}
    void BuildForMaster() const override;
{%- endif %}
    void Build() const override;
};

#endif
