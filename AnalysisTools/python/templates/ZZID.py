from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

import FWCore.ParameterSet.Config as cms


class ZZID(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        super(ZZID, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(ZZID, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'embedding':
            eIDEmbedder = cms.EDProducer(
                "PATElectronZZIDEmbedder",
                src = step.getObjTag('e'),
                idLabel = cms.string(self.getZZIDLabel()),
                vtxSrc = step.getObjTag('v'),
                bdtLabel = cms.string('MVAIDNonTrig'),
                idCutLowPtLowEta = cms.double(-.211),
                idCutLowPtMedEta = cms.double(-.396),
                idCutLowPtHighEta = cms.double(-.215),
                idCutHighPtLowEta = cms.double(-.870),
                idCutHighPtMedEta = cms.double(-.838),
                idCutHighPtHighEta = cms.double(-.763),
                missingHitsCut = cms.int32(999),
                ptCut = cms.double(7.), 
                )

            mIDEmbedder = cms.EDProducer(
                "PATMuonZZIDEmbedder",
                src = step.getObjTag('m'),
                vtxSrc = step.getObjTag('v'),
                ptCut = cms.double(5.),
                idLabel = cms.string(self.getZZIDLabel()),
                )

            #2l2j

            jIDEmbedder = cms.EDProducer(
                "PATJetIDEmbedder",
                src = step.getObjTag('j'),
                vtxSrc = step.getObjTag('v'),
                ptCut = cms.double(5.),
                idLabel = cms.string(self.getZZIDLabel()),
                )

            step.addModule("jIDEmbedder", jIDEmbedder, 'j') #2l2j
            step.addModule("eZZIDEmbedder", eIDEmbedder, 'e')
            step.addModule("mZZIDEmbedder", mIDEmbedder, 'm')

        return step

    def getZZIDLabel(self):
        return 'ZZIDPass'
