#ifndef PhysicsList_h
#define PhysicsList_h 1

#include "G4VModularPhysicsList.hh"

// Custom modular physics list
// Alternative: You can use G4PhysListFactory to select pre-built physics lists
// Example in main.cc:
//   #include "G4PhysListFactory.hh"
//   G4PhysListFactory factory;
//   auto physicsList = factory.GetReferencePhysList("QBBC");
//   runManager->SetUserInitialization(physicsList);

class PhysicsList : public G4VModularPhysicsList
{
public:
    PhysicsList();
    ~PhysicsList() override = default;
};

#endif
