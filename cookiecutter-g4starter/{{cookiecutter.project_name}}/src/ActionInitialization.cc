#include "ActionInitialization.hh"
#include "PrimaryGeneratorAction.hh"

{%- if cookiecutter.use_multithreading == "true" %}
void ActionInitialization::BuildForMaster() const
{
    // Actions for master thread (if needed)
}
{%- endif %}

void ActionInitialization::Build() const
{
    SetUserAction(new PrimaryGeneratorAction);
}
