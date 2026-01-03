#ifndef SteppingAction_h
#define SteppingAction_h 1

#include "G4UserSteppingAction.hh"
#include "G4Step.hh"

class SteppingAction : public G4UserSteppingAction
{
public:
    SteppingAction() = default;
    ~SteppingAction() override = default;

    void UserSteppingAction(const G4Step* step) override;
};

#endif
