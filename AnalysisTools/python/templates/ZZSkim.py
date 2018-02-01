from UWVV.AnalysisTools.AnalysisFlowBase import AnalysisFlowBase
from UWVV.AnalysisTools.templates.ZPlusXBaseFlow import ZPlusXBaseFlow
from UWVV.AnalysisTools.templates.ZZInitialStateBaseFlow import ZZInitialStateBaseFlow

import FWCore.ParameterSet.Config as cms


class ZZSkim(AnalysisFlowBase):
    def __init__(self, *args, **kwargs):
        super(ZZSkim, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(ZZSkim, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'selection':
            step.addBasicSelector('e', 'userFloat("{}") > 0.5'.format(self.getZZIDLabel()+'NoVtx'))
            step.addBasicSelector('m', 'userFloat("{}") > 0.5'.format(self.getZZIDLabel()+'NoVtx'))
            #step.addBasicSelector('j', 'userFloat("{}") > 0.5'.format(self.getZZIDLabel()+'NoVtx')) #2l2j

        if stepName == 'intermediateStateSelection':
            if isinstance(self, ZPlusXBaseFlow):
                step.addBasicSelector('ee', 'mass > 4. && mass < 120.')
                step.addBasicSelector('mm', 'mass > 4. && mass < 120.')
                step.addBasicSelector('jj', 'mass > 4. && mass < 120.') #2l2j

        if stepName == 'initialStateSelection':
            if isinstance(self, ZZInitialStateBaseFlow):
                step.addBasicSelector('eeee', 'daughter(0).mass > 40. || daughter(1).mass > 40.')
                step.addBasicSelector('eemm', 'daughter(0).mass > 40. || daughter(1).mass > 40.')
                step.addBasicSelector('mmmm', 'daughter(0).mass > 40. || daughter(1).mass > 40.')
                step.addBasicSelector('eejj', 'daughter(0).mass > 40. || daughter(1).mass > 40.') #2l2j
                step.addBasicSelector('mmjj', 'daughter(0).mass > 40. || daughter(1).mass > 40.') #2l2j

        return step


