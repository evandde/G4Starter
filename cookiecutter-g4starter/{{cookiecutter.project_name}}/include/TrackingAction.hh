#ifndef TrackingAction_h
#define TrackingAction_h 1

#include "G4UserTrackingAction.hh"
#include "G4Track.hh"

class TrackingAction : public G4UserTrackingAction
{
public:
    TrackingAction() = default;
    ~TrackingAction() override = default;

    void PreUserTrackingAction(const G4Track* track) override;
    void PostUserTrackingAction(const G4Track* track) override;
};

#endif
