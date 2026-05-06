#!/bin/bash 

if [ $# -ne 3 ]; then
    echo "Usage: $0 <paramfile> <field_list> <subrun>"
    exit
fi

paramfile=$1
fieldlist=$2
subrun=$3

GULLS_BASE_DIR=/home/crisp.92/Programs/gulls/
echo "sbatch --export='paramfile=$paramfile,fieldlist=$fieldlist,subrun=$subrun' ${GULLS_BASE_DIR}scripts/launchGULLSParallel.sh $paramfile $fieldlist $subrun"
sbatch --export="paramfile=$paramfile,fieldlist=$fieldlist,subrun=$subrun" ${GULLS_BASE_DIR}scripts/launchGULLSParallel.sh $paramfile $fieldlist $subrun

exit