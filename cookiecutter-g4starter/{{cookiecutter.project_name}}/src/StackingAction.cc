#include "StackingAction.hh"

G4ClassificationOfNewTrack StackingAction::ClassifyNewTrack(const G4Track* track)
{
    return fUrgent;
}
