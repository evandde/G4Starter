#ifndef StackingAction_h
#define StackingAction_h 1

#include "G4UserStackingAction.hh"
#include "G4ClassificationOfNewTrack.hh"
#include "G4Track.hh"

class StackingAction : public G4UserStackingAction
{
public:
    StackingAction() = default;
    ~StackingAction() override = default;

    G4ClassificationOfNewTrack ClassifyNewTrack(const G4Track* track) override;
};

#endif
