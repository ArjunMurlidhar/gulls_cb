#!/bin/bash

#module load mamba
#mamba activate gulls
conda activate gulls

paramfile=$1
fieldlist=$2
subrun=$3

save_filenum=0

date
echo $paramfile
echo $fieldlist
echo $subrun

echo "Exporting variables..."
source ~/.bashrc
gullsbin=${GULLS_BASE_DIR}bin
source ${GULLS_BASE_DIR}scripts/gullsPreamble_new.sh

echo RUNNAME $runname
echo OUTPUTDIR $outputdir
echo FINALDIR $finaldir
echo executable $executable
echo paramfile $paramfile
echo sflist $sfdir$sflist
echo srclist $srcdir$srclist
echo lenslist $lensdir$lenslist


awk -F ',' '{print $1}' $fieldlist | while read f; do
    read idx l b rest < <(grep "^$f " $srcdir/$srclist)
    echo From field list: $f $idx $l $b

    if [ $(grep "^$f " $srcdir/$srclist | wc -l) -eq 1 ] && [ $(grep "^$f " $lensdir/$lenslist | wc -l) -eq 1 ] && [ $(grep "^$f " $sfdir/$sflist | wc -l) -eq 5 ]; then
	echo Passes src/lens/sf check: $f $l $b;
        logfile=/home/crisp.92/launchpad/${runname}_${subrun}_${f}.logout
    	echo $gullsbin/$executable -d -d -d -d -i $paramfile -s $subrun -f $f > $logfile 2>&1
        $gullsbin/$executable -i $paramfile -s $subrun -f $f > $logfile 2>&1
	echo "GULLS field $f subrun $subrun simulations complete."
	
        if [ $save_filenum -eq 1 ]; then
            # NEED TO ADD RAW TO THIS
            echo Preserving file number limit by packaging data products...
            (cd $outputdir && tar -czf $finaldir/$runname/${runname}_${subrun}_${f}.fits.tar.gz $runname/${runname}_${subrun}_${f}_*.*.fits)
            rm $outputdir/$runname/${runname}_${subrun}_${f}_*.*.fits
            (cd $outputdir && tar -czf $finaldir/$runname/${runname}_${subrun}_${f}.lc.tar.gz $runname/${runname}_${subrun}_${f}_*.*.lc)
            rm $outputdir/$runname/${runname}_${subrun}_${f}_*.*.lc
            (cd $outputdir && tar -czf $finaldir/$runname/${runname}_${subrun}_${f}.fm.tar.gz $runname/${runname}_${subrun}_${f}_*.*.fm.*)
            rm $outputdir/$runname/${runname}_${subrun}_${f}_*.*.fm.*
            mv $outputdir/$runname/${runname}_${subrun}_${f}.* $finaldir/$runname/

	else
	    echo Transferring files...
	    mv -v $outputdir$runname/*.out $finaldir$runname/raw/
	    mv -v $outputdir$runname/*.log $finaldir$runname/raw/
	    mv -v $outputdir$runname/*.fits $finaldir$runname/images/
	    mv -v $outputdir$runname/*.lc $finaldir$runname/lc/
	    mv -v $outputdir$runname/*.fm $finaldir$runname/fm/
	fi
    else
        echo Field $f $l $b has incomplete starfields
    fi
done

