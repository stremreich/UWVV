from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase
from UWVV.AnalysisTools.templates.ZPlusXBaseFlow import ZPlusXBaseFlow
from UWVV.AnalysisTools.templates.ZZInitialStateBaseFlow import ZZInitialStateBaseFlow

import FWCore.ParameterSet.Config as cms


class ZZFSR(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'isMC'):
            self.isMC = kwargs.pop('isMC', True)
        super(ZZFSR, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(ZZFSR, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'embedding':
            leptonFSREmbedder = cms.EDProducer(
                "PATObjectFSREmbedder",
                muSrc = step.getObjTag('m'),
                eSrc = step.getObjTag('e'),
                candSrc = step.getObjTag('pfCands'),
                phoSelection = cms.string("pt > 2 && abs(eta) < 2.4"),
                nIsoSelection = cms.string("pt > 0.5"),
                chIsoSelection = cms.string("pt > 0.2"),
                eSelection = cms.string('userFloat("%s") > 0.5'%self.getZZIDLabel()),
                muSelection = cms.string('userFloat("%s") > 0.5'%self.getZZIDLabel()),
                fsrLabel = cms.string(self.getFSRLabel()),
                etPower = cms.double(2.),
                maxDR = cms.double(0.5),
                isoDR = cms.double(0.3),
                nIsoVetoDR = cms.double(0.01),
                chIsoVetoDR = cms.double(0.0001),
                relIsoCut = cms.double(1.8),
                eMuCrossCleaningDR = cms.double(0.05),
                )
            step.addModule('fsrEmbedder', leptonFSREmbedder, 'e', 'm')

        if stepName == 'selection':
            jetFSRCleaner = cms.EDProducer(
                'PATJetFSRCleaner',
                src = step.getObjTag('j'),
                srcE = step.getObjTag('e'),
                srcMu = step.getObjTag('m'),
                fsrLabel = cms.string(self.getFSRLabel()),
                fsrElecSelection = cms.string('userFloat("%sTight") > 0.5 && userFloat("%s") > 0.5'%(self.getZZIDLabel(), self.getZZIsoLabel())),
                fsrMuonSelection = cms.string('userFloat("%sTight") > 0.5 && userFloat("%s") > 0.5'%(self.getZZIDLabel(), self.getZZIsoLabel())),
                )
            step.addModule('jetFSRCleaner', jetFSRCleaner, 'j')
            
            if self.isMC:
                jetFSRCleaner_jesUp = jetFSRCleaner.clone(src = step.getObjTag('j_jesUp'))
                step.addModule('jetFSRCleanerJESUp', jetFSRCleaner_jesUp, 'j_jesUp')
                jetFSRCleaner_jesDown = jetFSRCleaner.clone(src = step.getObjTag('j_jesDown'))
                step.addModule('jetFSRCleanerJESDown', jetFSRCleaner_jesDown, 'j_jesDown')
                jetFSRCleaner_jerUp = jetFSRCleaner.clone(src = step.getObjTag('j_jerUp'))
                step.addModule('jetFSRCleanerJERUp', jetFSRCleaner_jerUp, 'j_jerUp')
                jetFSRCleaner_jerDown = jetFSRCleaner.clone(src = step.getObjTag('j_jerDown'))
                step.addModule('jetFSRCleanerJERDown', jetFSRCleaner_jerDown, 'j_jerDown')

        if stepName == 'intermediateStateEmbedding':
            if isinstance(self, ZPlusXBaseFlow):
                zeFSREmbedder = cms.EDProducer(
                    'PATElectronCompositeUserCandPromoter',
                    src = step.getObjTag('ee'),
                    label = cms.string(self.getFSRLabel()),
                    )
                zmFSREmbedder = cms.EDProducer(
                    'PATMuonCompositeUserCandPromoter',
                    src = step.getObjTag('mm'),
                    label = cms.string(self.getFSRLabel()),
                    )

                step.addModule('zeFSREmbedder', zeFSREmbedder, 'ee')
                step.addModule('zmFSREmbedder', zmFSREmbedder, 'mm')

                #2l2j
                
                zjFSREmbedder = cms.EDProducer(
                    'PATJetCompositeUserCandPromoter',
                    src = step.getObjTag('jj'),
                    label = cms.string(self.getFSRLabel()),
                    )

                step.addModule('zjFSREmbedder', zjFSREmbedder, 'jj')

                #2l2j

        return step

    def getFSRLabel(self):
        return "fsr"
