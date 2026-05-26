#!/bin/bash 

if [ $# -ne 3 ]; then
    echo "Usage: $0 <paramfile> <field> <subrun>"
    exit
fi

paramfile=$1
field=$2
subrun=$3

GULLS_BASE_DIR=/users/PAS3230/arjunm/gulls/gulls_cb/
paramname=$(basename "$paramfile" .prm)
scriptout=/fs/scratch/PAS3230/gulls_logs/${paramname}_${field}_${subrun}.scriptout
echo "sbatch --export='paramfile=$paramfile,field=$field, subrun=$subrun' ${GULLS_BASE_DIR}run/runGULLSSingleField.sh $paramfile $field $subrun"
sbatch -A PAS3230 --output="$scriptout" --export="paramfile=$paramfile,field=$field,subrun=$subrun" ${GULLS_BASE_DIR}run/runGULLSSingleField.sh $paramfile $field $subrun 

exit
