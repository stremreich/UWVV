#!/bin/bash
cmsRun UWVV/Ntuplizer/test/ntuplize_cfg.py \
    inputFiles=file:00AE1CAD-E1E0-E611-9C36-0025905A60B0.root \
    datasetName=ZZTo4L_13TeV_powheg_pythia8 \
    outputFile=testZZMC.root \
    channels=zz \
    isMC=1 \
    eCalib=1 \
    muCalib=1 \
    lheWeights=3 \
    globalTag=80X_mcRun2_asymptotic_2016_TrancheIV_v7 \
    $1
