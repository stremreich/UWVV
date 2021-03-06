//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//   PATElectronSystematicShifter.cc                                        //
//                                                                          //
//   Takes an electron collection from MC and shifts the electrons' energy  //
//   by the scale and/or resolution uncertainties for systematics           //
//   calculations.                                                          //
//                                                                          //
//   Nate Woods, U. Wisconsin                                               //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


// system includes
#include <memory>
#include <vector>

// CMS includes
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "EgammaAnalysis/ElectronTools/interface/EnergyScaleCorrection_class.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"
#include "CLHEP/Random/RandGauss.h"

// #include "EgammaAnalysis/ElectronTools/interface/SimpleElectron.h"

class PATElectronSystematicShifter : public edm::stream::EDProducer<>
{
public:
  explicit PATElectronSystematicShifter(const edm::ParameterSet&);
  virtual ~PATElectronSystematicShifter() {}

private:
  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);

  const edm::EDGetTokenT<edm::View<pat::Electron> > electronCollectionToken;
  const std::string filename; // files to base the corrections on (same as with CalibratedPatElectronProducerRun2)

  // Size of shift, in units of sigma
  const float scaleShift;
  const float rhoResShift;
  const float phiResShift;

  const EnergyScaleCorrection_class correcter;
};



PATElectronSystematicShifter::PATElectronSystematicShifter(const edm::ParameterSet& iConfig):
  electronCollectionToken(consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("src"))),
  filename(iConfig.getParameter<std::string>("correctionFile")),
  scaleShift(iConfig.exists("scaleShift") ? iConfig.getParameter<double>("scaleShift") : 0.),
  rhoResShift(iConfig.exists("rhoResShift") ? iConfig.getParameter<double>("rhoResShift") : 0.),
  phiResShift(iConfig.exists("phiResShift") ? iConfig.getParameter<double>("phiResShift") : 0.),
  correcter(filename)
{
  edm::Service<edm::RandomNumberGenerator> rng;
  if(!rng.isAvailable())
    throw cms::Exception("Configuration")
      << "PATElectronSystematicShifter requires the "
      << "RandomNumberGeneratorService, which is not present in this "
      << "configuration!" << std::endl
      << "Please add it!" << std::endl;

  produces<std::vector<pat::Electron> >();
}


void PATElectronSystematicShifter::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::unique_ptr<std::vector<pat::Electron> > out = std::make_unique<std::vector<pat::Electron> >();

  edm::Handle<edm::View<pat::Electron> > in;

  iEvent.getByToken(electronCollectionToken, in);

  edm::Service<edm::RandomNumberGenerator> rng;
  CLHEP::HepRandomEngine& engine = rng->getEngine(iEvent.streamID());

  for(size_t iEle = 0; iEle < in->size(); ++iEle)
    {
      out->push_back(in->at(iEle));
      pat::Electron& ele = out->back();

      // using simple electron fixes some problems, not sure why...
      // SimpleElectron simp(ele, 1, true);
      // bool isEB = simp.isEB();
      // float r9 = simp.getR9();
      // float absEta = std::abs(simp.getEta());
      // float et = simp.getNewEnergy() / cosh(absEta);

      bool isEB = ele.isEB();
      float r9 = ele.r9();
      float absEta = std::abs(ele.eta());
      float et = ele.et();

      float scale = 1.;

      if(scaleShift)
        {
          float scaleError =
            correcter.ScaleCorrectionUncertainty(iEvent.id().run(),
                                                 isEB, r9, absEta, et);

          // flip sign of shift because we're "undoing" the correction applied
          // to data
          scale -= scaleShift * scaleError;
        }

      if(rhoResShift != 0. || phiResShift != 0.)
        {
          float smearSigma =
            correcter.getSmearingSigma(iEvent.id().run(), isEB, r9, absEta,
                                       et, rhoResShift, phiResShift);

          scale = CLHEP::RandGauss::shoot(&engine, scale, smearSigma);
        }

      ele.setP4(math::PtEtaPhiMLorentzVector(scale*ele.pt(), ele.eta(),
                                             ele.phi(), ele.mass()));
    }

  iEvent.put(std::move(out));
}

DEFINE_FWK_MODULE(PATElectronSystematicShifter);
