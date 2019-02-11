#!/bin/bash
#igprof -d -mp -z -o igprof.mp.gz 
cmsRun UWVV/Ntuplizer/test/ntuplize_cfg.py \
    inputFiles=/store/mc/RunIIFall17MiniAODv2/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/90000/DEAB067D-14A3-E811-B650-FA163EC3AAC6.root \
    datasetName=WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8 \
    outputFile=testMCWZ_QCD.root \
    channels=wz \
    isMC=1 \
    eCalib=1 \
    muCalib=1 \
    lheWeights=3 \
    globalTag=94X_mc2017_realistic_v14 \
    $1
