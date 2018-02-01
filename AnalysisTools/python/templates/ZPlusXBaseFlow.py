from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

import FWCore.ParameterSet.Config as cms


class ZPlusXBaseFlow(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        super(ZPlusXBaseFlow, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(ZPlusXBaseFlow, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'intermediateStateCreation':
            self.addZCreation(step)

        return step


    def addZCreation(self, step):
        '''
        Add modules to make Z candidates
        '''
        zEEMod = cms.EDProducer(
            'PATCandViewShallowCloneCombiner',
            decay = cms.string('{0}@+ {0}@-'.format(step.getObjTagString('e'))),
            roles = cms.vstring('e1', 'e2'),
            cut = cms.string(self.__class__.getZEECuts()),
            checkCharge = cms.bool(True),
            setPdgId = cms.int32(23),
            )

        zMuMuMod = cms.EDProducer(
            'PATCandViewShallowCloneCombiner',
            decay = cms.string('{0}@+ {0}@-'.format(step.getObjTagString('m'))),
            roles = cms.vstring('m1', 'm2'),
            cut = cms.string(self.__class__.getZMMCuts()),
            checkCharge = cms.bool(True),
            setPdgId = cms.int32(23),
            )

        step.addModule("zEECreation", zEEMod, 'ee')
        step.addModule("zMuMuCreation", zMuMuMod, 'mm')

        #2l2j
        
        zJetJetMod = cms.EDProducer(
            'PATCandViewShallowCloneCombiner',
            decay = cms.string('{0}@+ {0}@-'.format(step.getObjTagString('j'))),
            roles = cms.vstring('j1', 'j2'),
            cut = cms.string(self.__class__.getZJetJetCuts()),
            checkCharge = cms.bool(True),
            setPdgId = cms.int32(23),
            )

        step.addModule("zJetJetCreation", zJetJetMod, 'jj')


    @classmethod
    def getZEECuts(cls):
        return ('daughter("e1").pt > 7 && '
                'daughter("e2").pt > 7 && '
                'abs(daughter("e1").eta) < 2.5 && '
                'abs(daughter("e2").eta) < 2.5')


    @classmethod
    def getZMMCuts(cls):
        return ('daughter("m1").pt > 5 && '
                'daughter("m2").pt > 5 && '
                'abs(daughter("m1").eta) < 2.4 && '
                'abs(daughter("m2").eta) < 2.4')

    #2l2j
    @classmethod
    def getZJetJetCuts(cls):
        return('')
        #return ('daughter("j1").pt > 5 && '
        #        'daughter("j2").pt > 5 && '
        #        'abs(daughter("j1").eta) < 2.4 && '
        #        'abs(daughter("j2").eta) < 2.4')


class ZPlusXBaseFlowGen(ZPlusXBaseFlow):
    @classmethod
    def getZEECuts(cls):
        return ('daughter("e1").pt > 5 && '
                'daughter("e2").pt > 5 && '
                'abs(daughter("e1").eta) < 2.5 && '
                'abs(daughter("e2").eta) < 2.5')


    @classmethod
    def getZMMCuts(cls):
        return ('daughter("m1").pt > 5 && '
                'daughter("m2").pt > 5 && '
                'abs(daughter("m1").eta) < 2.5 && '
                'abs(daughter("m2").eta) < 2.5')

    #2l2j
    @classmethod
    def getZJetJetCuts(cls):
        return ('daughter("j1").pt > 5 && '
                'daughter("j2").pt > 5 && '
                'abs(daughter("j1").eta) < 2.4 && '
                'abs(daughter("j2").eta) < 2.4')
