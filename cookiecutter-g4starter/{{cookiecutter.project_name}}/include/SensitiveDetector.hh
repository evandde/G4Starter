{%- if cookiecutter.sd_class_name -%}
#ifndef {{ cookiecutter.sd_class_name }}_h
#define {{ cookiecutter.sd_class_name }}_h 1

#include "G4VSensitiveDetector.hh"

class G4Step;
class G4HCofThisEvent;

class {{ cookiecutter.sd_class_name }} : public G4VSensitiveDetector
{
public:
    {{ cookiecutter.sd_class_name }}(const G4String& name);
    ~{{ cookiecutter.sd_class_name }}() override;

    void Initialize(G4HCofThisEvent* hitCollection) override;
    G4bool ProcessHits(G4Step* step, G4TouchableHistory* history) override;
    void EndOfEvent(G4HCofThisEvent* hitCollection) override;
};

#endif
{%- endif %}
