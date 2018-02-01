from UWVV.AnalysisTools.templates.JetQuarkGluonTagging import JetQuarkGluonTagging

import FWCore.ParameterSet.Config as cms


class ZZClassification(JetQuarkGluonTagging):
    def __init__(self, *args, **kwargs):
        super(ZZClassification, self).__init__(*args, **kwargs)

    def makeAnalysisStep(self, stepName, **inputs):
        step = super(ZZClassification, self).makeAnalysisStep(stepName, **inputs)

        if stepName == 'initialStateEmbedding':
            meEmbedding4e = cms.EDProducer(
                "ZZDiscriminantEmbedderEEEE",
                src = step.getObjTag('eeee'),
                jetSrc = step.getObjTag('j'),
                fsrLabel = cms.string(self.getFSRLabel()),
                qgDiscriminator = cms.string(self.qgLikelihoodLabel()),
                skimDecisionLabels = cms.vstring(
                    '{}Tight'.format(self.getZZIDLabel()),
                    self.getZZIsoLabel(),
                    ),
                )
            step.addModule('meEmbedding4e', meEmbedding4e, 'eeee')
                
            meEmbedding2e2m = cms.EDProducer(
                "ZZDiscriminantEmbedderEEMM",
                src = step.getObjTag('eemm'),
                jetSrc = step.getObjTag('j'),
                fsrLabel = cms.string(self.getFSRLabel()),
                qgDiscriminator = cms.string(self.qgLikelihoodLabel()),
                skimDecisionLabels = cms.vstring(
                    '{}Tight'.format(self.getZZIDLabel()),
                    self.getZZIsoLabel(),
                    ),
                )
            step.addModule('meEmbedding2e2m', meEmbedding2e2m, 'eemm')
                
            meEmbedding4m = cms.EDProducer(
                "ZZDiscriminantEmbedderMMMM",
                src = step.getObjTag('mmmm'),
                jetSrc = step.getObjTag('j'),
                fsrLabel = cms.string(self.getFSRLabel()),
                qgDiscriminator = cms.string(self.qgLikelihoodLabel()),
                skimDecisionLabels = cms.vstring(
                    '{}Tight'.format(self.getZZIDLabel()),
                    self.getZZIsoLabel(),
                    ),
                )
            step.addModule('meEmbedding4m', meEmbedding4m, 'mmmm')

            #2l2j
            
            meEmbedding2m2j = cms.EDProducer(
                "ZZDiscriminantEmbedderMMJetJet",
                src = step.getObjTag('mmjj'),
                jetSrc = step.getObjTag('j'),
                fsrLabel = cms.string(self.getFSRLabel()),
                qgDiscriminator = cms.string(self.qgLikelihoodLabel()),
                skimDecisionLabels = cms.vstring(
                    '{}Tight'.format(self.getZZIDLabel()),
                    self.getZZIsoLabel(),
                    ),
                )
            step.addModule('meEmbedding2m2j', meEmbedding2m2j, 'mmjj')

            categoryEmbedding2m2j = cms.EDProducer(
                'ZZCategoryEmbedder',
                src = step.getObjTag('mmjj'),
                electronSrc = step.getObjTag('e'),
                muonSrc = step.getObjTag('m'),
                jetSrc = step.getObjTag('j'),
                leptonSelection = cms.string('userFloat("{}Tight") > 0.5 && userFloat("{}") > 0.5'.format(self.getZZIDLabel(), self.getZZIsoLabel())),
                bDiscriminator = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
                bDiscriminatorCut = cms.double(0.800),
                )
            step.addModule('categoryEmbedding2m2j', categoryEmbedding2m2j, 'mmjj')

            #2l2j
                
            categoryEmbedding4e = cms.EDProducer(
                'ZZCategoryEmbedder',
                src = step.getObjTag('eeee'),
                electronSrc = step.getObjTag('e'),
                muonSrc = step.getObjTag('m'),
                jetSrc = step.getObjTag('j'),
                leptonSelection = cms.string('userFloat("{}Tight") > 0.5 && userFloat("{}") > 0.5'.format(self.getZZIDLabel(), self.getZZIsoLabel())),
                bDiscriminator = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
                bDiscriminatorCut = cms.double(0.800),
                )
            step.addModule('categoryEmbedding4e', categoryEmbedding4e, 'eeee')

            categoryEmbedding2e2m = cms.EDProducer(
                'ZZCategoryEmbedder',
                src = step.getObjTag('eemm'),
                electronSrc = step.getObjTag('e'),
                muonSrc = step.getObjTag('m'),
                jetSrc = step.getObjTag('j'),
                leptonSelection = cms.string('userFloat("{}Tight") > 0.5 && userFloat("{}") > 0.5'.format(self.getZZIDLabel(), self.getZZIsoLabel())),
                bDiscriminator = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
                bDiscriminatorCut = cms.double(0.800),
                )
            step.addModule('categoryEmbedding2e2m', categoryEmbedding2e2m, 'eemm')

            categoryEmbedding4m = cms.EDProducer(
                'ZZCategoryEmbedder',
                src = step.getObjTag('mmmm'),
                electronSrc = step.getObjTag('e'),
                muonSrc = step.getObjTag('m'),
                jetSrc = step.getObjTag('j'),
                leptonSelection = cms.string('userFloat("{}Tight") > 0.5 && userFloat("{}") > 0.5'.format(self.getZZIDLabel(), self.getZZIsoLabel())),
                bDiscriminator = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
                bDiscriminatorCut = cms.double(0.800),
                )
            step.addModule('categoryEmbedding4m', categoryEmbedding4m, 'mmmm')


        return step

