#!/bin/bash
cmsRun UWVV/Ntuplizer/test/ntuplize_cfg.py \
    inputFiles=/store/mc/RunIIFall17MiniAOD/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v2/60000/FC8BCD89-E7D6-E711-BD5D-0242AC1C0501.root \
    datasetName=ZZTo4L_13TeV_powheg_pythia8 \
    outputFile=testMCWZ_ZZ4L.root \
    channels=wz \
    isMC=1 \
    eCalib=1 \
    muCalib=1 \
    lheWeights=3 \
    globalTag=94X_mc2017_realistic_v14 \
    $1




