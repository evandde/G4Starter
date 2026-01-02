#include "StackingAction.hh"

G4ClassificationOfNewTrack StackingAction::ClassifyNewTrack(const G4Track* aTrack)
{
    return fUrgent;
}
