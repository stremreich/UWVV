#!/bin/bash
#igprof -d -mp -z -o igprof.mp.gz 
cmsRun UWVV/Ntuplizer/test/ntuplize_cfg.py \
    inputFiles=/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/BA64B6FA-B04E-E811-B940-00000086FE80.root \
    datasetName=WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8 \
    outputFile=testMCWZ.root \
    channels=wz \
    isMC=1 \
    eCalib=1 \
    muCalib=0 \
    lheWeights=3 \
    globalTag= \
    $1
