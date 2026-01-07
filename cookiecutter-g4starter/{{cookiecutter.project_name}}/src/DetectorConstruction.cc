#include "DetectorConstruction.hh"

#include "G4SystemOfUnits.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"

G4VPhysicalVolume *DetectorConstruction::Construct()
{
    // materials
    auto nist = G4NistManager::Instance();
    auto airMat = nist->FindOrBuildMaterial("G4_AIR");

    // World
    auto worldSize = 1. * m;
    auto worldSol = new G4Box("World", .5 * worldSize, .5 * worldSize, .5 * worldSize);
    auto worldLog = new G4LogicalVolume(worldSol, airMat, "World");
    auto worldPhys = new G4PVPlacement(0, G4ThreeVector(), worldLog, "World", nullptr, false, 0);

    return worldPhys;
}

void DetectorConstruction::ConstructSDandField()
{
}
