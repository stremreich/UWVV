from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase

import FWCore.ParameterSet.Config as cms

class MuonCalibration(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        self.isMC = kwargs.get('isMC', True)
        self.isSync = self.isMC and kwargs.get('isSync', False)
        super(MuonCalibration, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(MuonCalibration, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'preliminary':
            if self.isMC:
                calibType = 'MC_76X_13TeV'
            else:
                calibType = 'DATA_76X_13TeV'

            muCalibrator = cms.EDProducer(
                "PATMuonKalmanCorrector",
                src = step.getObjTag('m'),
                calibType = cms.string(calibType),
                isMC = cms.bool(self.isMC),
                isSync = cms.bool(self.isSync),
                )

            step.addModule('calibratedPatMuons', muCalibrator, 'm')

        return step


    




