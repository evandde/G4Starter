#include "PhysicsList.hh"

// =============================================================================
// Custom Modular Physics List
// =============================================================================
// This file provides a template for building a custom physics list by
// selecting individual physics builders (modular approach).
//
// ALTERNATIVE APPROACH: G4PhysListFactory
// ---------------------------------------
// Instead of creating a custom PhysicsList class, you can use G4PhysListFactory
// to select from pre-built reference physics lists. To use this approach:
//
// 1. Delete this PhysicsList.hh/.cc
// 2. In main.cc, replace:
//      #include "PhysicsList.hh"
//      runManager->SetUserInitialization(new PhysicsList);
//    with:
//      #include "G4PhysListFactory.hh"
//      G4PhysListFactory factory;
//      auto physicsList = factory.GetReferencePhysList("QBBC");
//      runManager->SetUserInitialization(physicsList);
//
// Available reference physics lists (select one):
//   - QBBC: General purpose (recommended for most users)
//   - FTFP_BERT: High energy physics
//   - FTFP_BERT_HP: With high precision neutrons
//   - QGSP_BERT: Alternative HEP list
//   - QGSP_BERT_HP: With high precision neutrons
//   - QGSP_BIC: Binary cascade
//   - QGSP_BIC_HP: Binary cascade with HP neutrons
//   - Shielding: Radiation shielding applications
//   - NuBeam: Neutrino beam experiments
//
// =============================================================================

// Uncomment the physics builders you need:

// Standard electromagnetic physics options
// #include "G4EmStandardPhysics.hh"
// #include "G4EmStandardPhysics_option1.hh"
// #include "G4EmStandardPhysics_option2.hh"
// #include "G4EmStandardPhysics_option3.hh"
// #include "G4EmStandardPhysics_option4.hh"

// Low energy electromagnetic physics (Livermore, Penelope)
// #include "G4EmLivermorePhysics.hh"
// #include "G4EmPenelopePhysics.hh"
// #include "G4EmLowEPPhysics.hh"

// DNA physics for micro/nanodosimetry
// #include "G4EmDNAPhysics.hh"
// #include "G4EmDNAPhysics_option2.hh"

// Decay physics
// #include "G4DecayPhysics.hh"
// #include "G4RadioactiveDecayPhysics.hh"

// Hadronic physics
// #include "G4HadronElasticPhysicsHP.hh"
// #include "G4HadronPhysicsFTFP_BERT.hh"
// #include "G4HadronPhysicsFTFP_BERT_HP.hh"
// #include "G4HadronPhysicsQGSP_BERT.hh"
// #include "G4HadronPhysicsQGSP_BERT_HP.hh"
// #include "G4HadronPhysicsQGSP_BIC.hh"
// #include "G4HadronPhysicsQGSP_BIC_HP.hh"

// Ion physics
// #include "G4IonPhysics.hh"
// #include "G4IonElasticPhysics.hh"
// #include "G4IonPhysicsPHP.hh"
// #include "G4IonINCLXXPhysics.hh"

// Stopping and extra physics
// #include "G4StoppingPhysics.hh"
// #include "G4EmExtraPhysics.hh"

// Optical physics
// #include "G4OpticalPhysics.hh"

PhysicsList::PhysicsList()
    : G4VModularPhysicsList()
{
    // Set default cut value
    SetDefaultCutValue(0.7 * CLHEP::mm);

    // =================================================================
    // Uncomment and register the physics you need
    // =================================================================

    // -----------------------------------------------------------------
    // Electromagnetic Physics
    // -----------------------------------------------------------------
    // Standard EM (choose one):
    // RegisterPhysics(new G4EmStandardPhysics());              // Default
    // RegisterPhysics(new G4EmStandardPhysics_option1());      // Fast simulation
    // RegisterPhysics(new G4EmStandardPhysics_option2());      // Experimental
    // RegisterPhysics(new G4EmStandardPhysics_option3());      // Best for HEP
    // RegisterPhysics(new G4EmStandardPhysics_option4());      // Most accurate

    // Low energy EM (choose one if needed):
    // RegisterPhysics(new G4EmLivermorePhysics());             // For low E (< 1 GeV)
    // RegisterPhysics(new G4EmPenelopePhysics());              // For low E alternative
    // RegisterPhysics(new G4EmLowEPPhysics());                 // Polarized processes

    // DNA physics (for micro/nanodosimetry):
    // RegisterPhysics(new G4EmDNAPhysics());                   // DNA processes
    // RegisterPhysics(new G4EmDNAPhysics_option2());           // Alternative DNA

    // -----------------------------------------------------------------
    // Decay Physics
    // -----------------------------------------------------------------
    // RegisterPhysics(new G4DecayPhysics());                   // Particle decay

    // Radioactive decay (includes atomic relaxation):
    // RegisterPhysics(new G4RadioactiveDecayPhysics());        // Radioactive decay

    // Note: G4RadioactiveDecayPhysics includes:
    //   - Radioactive decay chains
    //   - Atomic relaxation (de-excitation)
    //   - Fluorescence photon emission
    //   - Auger electron emission
    //   - X-ray emission from atomic shells

    // -----------------------------------------------------------------
    // Hadronic Physics
    // -----------------------------------------------------------------
    // Elastic scattering:
    // RegisterPhysics(new G4HadronElasticPhysicsHP());         // High precision

    // Inelastic (choose one):
    // RegisterPhysics(new G4HadronPhysicsFTFP_BERT());         // Standard (E > 3 GeV)
    // RegisterPhysics(new G4HadronPhysicsFTFP_BERT_HP());      // With thermal neutrons
    // RegisterPhysics(new G4HadronPhysicsQGSP_BERT());         // Alternative
    // RegisterPhysics(new G4HadronPhysicsQGSP_BERT_HP());      // With thermal neutrons
    // RegisterPhysics(new G4HadronPhysicsQGSP_BIC());          // Binary cascade
    // RegisterPhysics(new G4HadronPhysicsQGSP_BIC_HP());       // With thermal neutrons

    // -----------------------------------------------------------------
    // Ion Physics
    // -----------------------------------------------------------------
    // RegisterPhysics(new G4IonPhysics());                     // Standard ion physics
    // RegisterPhysics(new G4IonElasticPhysics());              // Ion elastic scattering
    // RegisterPhysics(new G4IonPhysicsPHP());                  // Particle HP ions
    // RegisterPhysics(new G4IonINCLXXPhysics());               // INCL++ model

    // -----------------------------------------------------------------
    // Additional Physics
    // -----------------------------------------------------------------
    // RegisterPhysics(new G4StoppingPhysics());                // Stopping particles
    // RegisterPhysics(new G4EmExtraPhysics());                 // Gamma/muon nuclear, etc.
    // RegisterPhysics(new G4OpticalPhysics());                 // Optical photons

    // =================================================================
    // Example: Typical setup for medical physics simulation
    // =================================================================
    // RegisterPhysics(new G4EmStandardPhysics_option4());
    // RegisterPhysics(new G4EmExtraPhysics());
    // RegisterPhysics(new G4DecayPhysics());
    // RegisterPhysics(new G4RadioactiveDecayPhysics());
    // RegisterPhysics(new G4HadronElasticPhysicsHP());
    // RegisterPhysics(new G4HadronPhysicsQGSP_BIC_HP());
    // RegisterPhysics(new G4StoppingPhysics());
    // RegisterPhysics(new G4IonPhysics());

    // =================================================================
    // Example: Typical setup for high energy physics
    // =================================================================
    // RegisterPhysics(new G4EmStandardPhysics());
    // RegisterPhysics(new G4EmExtraPhysics());
    // RegisterPhysics(new G4DecayPhysics());
    // RegisterPhysics(new G4HadronElasticPhysicsHP());
    // RegisterPhysics(new G4HadronPhysicsFTFP_BERT());
    // RegisterPhysics(new G4StoppingPhysics());
    // RegisterPhysics(new G4IonPhysics());
}
