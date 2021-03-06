import FWCore.ParameterSet.Config as cms


wzCountBranches = cms.PSet(
    uints = cms.PSet(
        nCBVIDTightElec = cms.string('? hasUserInt("nCBVIDtightElec") ?'
                                     'userInt("nCBVIDtightElec") : 999'),
        nCBVIDMediumElec = cms.string('? hasUserInt("nCBVIDmediumElec") ?'
                                      'userInt("nCBVIDmediumElec") : 999'),
        nCBVIDLooseElec = cms.string('? hasUserInt("nCBVIDlooseElec") ?'
                                     'userInt("nCBVIDlooseElec") : 999'),
        nTightMuon = cms.string('? hasUserInt("nTightMuon") ? '
                                'userInt("nTightMuon") : 999'),
        nMediumMuonICHEP = cms.string('? hasUserInt("nMediumMuonICHEP") ? '
                                      'userInt("nMediumMuonICHEP") : 999'),
        nJetJPL = cms.string('? hasUserInt("nJetJPL") ? '
                              'userInt("nJetJPL") : 999'),
        nJetJPM = cms.string('? hasUserInt("nJetJPM") ? ' 
                              'userInt("nJetJPM") : -999'),
        nJetJPT = cms.string('? hasUserInt("nJetJPT") ? '
                              'userInt("nJetJPT") : -999'),
        nJetCSVv2L = cms.string('? hasUserInt("nJetCSVv2L") ? '
                              'userInt("nJetCSVv2L") : -999'),
        nJetCSVv2M = cms.string('? hasUserInt("nJetCSVv2M") ? '
                                 'userInt("nJetCSVv2M") : -999'),
        nJetCSVv2T = cms.string('? hasUserInt("nJetCSVv2T") ? '
                                 'userInt("nJetCSVv2T") : -999'),
        nJetCMVAv2L = cms.string('? hasUserInt("nJetCMVAv2L") ? '
                                  'userInt("nJetCMVAv2L") : -999'),
        nJetCMVAv2M = cms.string('? hasUserInt("nJetCMVAv2M") ? '
                                  'userInt("nJetCMVAv2M") : -999'),
        nJetCMVAv2T = cms.string('? hasUserInt("nJetCMVAv2T") ? '
                                  'userInt("nJetCMVAv2T") : -999'),
        ),
    )

zzCountBranches = cms.PSet(
    uints = cms.PSet(
        nZZLooseElec = cms.string('? hasUserInt("nZZLooseElectrons") ?'
                                  'userInt("nZZLooseElectrons") : 999'),
        nZZTightElec = cms.string('? hasUserInt("nZZTightElectrons") ?'
                                  'userInt("nZZTightElectrons") : 999'),
        nZZTightIsoElec = cms.string('? hasUserInt("nZZTightIsoElectrons") ?'
                                     'userInt("nZZTightIsoElectrons") : 999'),
        nZZLooseMu = cms.string('? hasUserInt("nZZLooseMuons") ?'
                                'userInt("nZZLooseMuons") : 999'),
        nZZTightMu = cms.string('? hasUserInt("nZZTightMuons") ?'
                                'userInt("nZZTightMuons") : 999'),
        nZZTightIsoMu = cms.string('? hasUserInt("nZZTightIsoMuons") ?'
                                   'userInt("nZZTightIsoMuons") : 999'),
        ),
    )

