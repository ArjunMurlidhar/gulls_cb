#!/bin/bash

# module load mamba
# mamba activate gulls
module load miniconda3/24.1.2-py310
conda activate gulls
module load gsl/2.7.1

paramfile=$1
field=$2
subrun=$3

save_filenum=0

date
echo $paramfile
echo $field
echo $subrun

echo "Exporting variables..."
source ~/.bashrc
gullsbin=${GULLS_BASE_DIR}/bin/
source ${GULLS_BASE_DIR}/scripts/gullsPreamble_new.sh

echo RUNNAME $runname
echo OUTPUTDIR $outputdir
echo FINALDIR $finaldir
echo executable $executable
echo paramfile $paramfile
echo sflist $sfdir$sflist
echo srclist $srcdir$srclist
echo lenslist $lensdir$lenslist


read idx l b rest < <(grep "^$field " $srcdir/$srclist)
echo From field list: $field $idx $l $b

if [ $(grep "^$field " $srcdir$srclist | wc -l) -eq 1 ] && [ $(grep "^$field " $lensdir$lenslist | wc -l) -eq 1 ] && [ $(grep "^$field " $sfdir$sflist | wc -l) -eq 5 ]; then
    echo Passes src/lens/sf check: $field $l $b;
    logfile=/fs/scratch/PAS3230/gulls_logs/${runname}_${subrun}_${field}.logout
    echo $gullsbin$executable -i $paramfile -s $subrun -f $field -d > $logfile 2>&1
    $gullsbin$executable -i $paramfile -s $subrun -f $field -d > $logfile 2>&1
    echo "GULLS field $field subrun $subrun simulations complete."
	
    if [ $save_filenum -eq 1 ]; then
        # NEED TO ADD RAW TO THIS
        echo Preserving file number limit by packaging data products...
        (cd $outputdir && tar -czf $finaldir$runname/${runname}_${subrun}_${field}.fits.tar.gz $runname/${runname}_${subrun}_${field}_*.*.fits)
        rm $outputdir$runname/${runname}_${subrun}_${field}_*.*.fits
        (cd $outputdir && tar -czf $finaldir$runname/${runname}_${subrun}_${field}.lc.tar.gz $runname/${runname}_${subrun}_${field}_*.*.lc)
        rm $outputdir$runname/${runname}_${subrun}_${field}_*.*.lc
        (cd $outputdir && tar -czf $finaldir$runname/${runname}_${subrun}_${field}.fm.tar.gz $runname/${runname}_${subrun}_${field}_*.*.fm.*)
        rm $outputdir$runname/${runname}_${subrun}_${field}_*.*.fm.*
        mv $outputdir$runname/${runname}_${subrun}_${field}.* $finaldir$runname/

    else
	echo Transferring files...
	mv -v $outputdir$runname/*.out $finaldir$runname/raw/
	mv -v $outputdir$runname/*.log $finaldir$runname/raw/
	mv -v $outputdir$runname/*.fits $finaldir$runname/images/
	mv -v $outputdir$runname/*.lc $finaldir$runname/lc/
	mv -v $outputdir$runname/*.fm $finaldir$runname/fm/
    fi
else
    echo Field $field $l $b has incomplete starfields
fi


