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
    auto matAir = nist->FindOrBuildMaterial("G4_AIR");

    // World
    auto worldSize = 1. * m;
    auto solWorld = new G4Box("World", .5 * worldSize, .5 * worldSize, .5 * worldSize);
    auto lvWorld = new G4LogicalVolume(solWorld, matAir, "World");
    auto pvWorld = new G4PVPlacement(0, G4ThreeVector(), lvWorld, "World", nullptr, false, 0);

    return pvWorld;
}

void DetectorConstruction::ConstructSDandField()
{
}
