#!/bin/bash

#This script performs all the housekeeping type setup required to run an gulls simulation
#It makes sure that the directory structure that gulls expects for output exists

#Load the common preamble
export SCRIPTDIR=${GULLS_BASE_DIR}/scripts/
source ${SCRIPTDIR}gullsPreamble_new.sh
#set location of executables, must be kept in this dir? Or give full dir in 
export SRCDIR=${GULLS_BASE_DIR}/bin/

#Setup output directory structure
#echo $finaldir, $SCRIPTDIR
#Make sure there is an output root directory
if [ ! -d $finaldir ]; then
   mkdir $finaldir
   echo Created $finaldir
fi


if [ ! -d $finaldir$runname ]; then
    mkdir $finaldir$runname
    echo Created $finaldir$runname
fi

#Make sure there are output subdirectories
for rt in $finaldir; do
    for direc in raw logs lc analysis fm images; do 
	diraim=$rt$runname/$direc
	if [ ! -d $diraim ]; then
	    mkdir $diraim
	    echo Created $diraim
	fi
    done
done

#Copy across the parameter files that were used

#the observatory list
cp -i -n -v $obslist $finaldir$runname/logs/

grep -v '^#' $obslist | grep -v '^$' | while read obs; do
    dotobs=$(echo $obs | awk '{print $1}')
    dotweather=$(echo $obs | awk -F'WEATHER_PROFILE=' '{print $2}' | awk '{print $1}')
    dotseq=$(echo $obs | awk -F'OBSERVATION_SEQUENCE=' '{print $2}' | awk '{print $1}')
    dotdet=$(echo $obs | awk -F'DETECTOR=' '{print $2}' | awk '{print $1}')
    # echo $dotobs; echo $dotweather; echo $dotseq; echo $dotdet
    echo "Copying across each file for $obs..."
    # Each observatory
    cp -i -n -v $obsdir$dotobs $finaldir$runname/logs/
    # Each weather profile
    cp -i -n -v $weatherdir$dotweather $finaldir$runname/logs/
    # Each observation sequence
    cp -i -n -v $obsdir$dotseq $finaldir$runname/logs/
    echo;echo;echo
done

echo "Copying across executable and parameter file..."
# Copy executable
cp -i -n -v $SRCDIR$executable $finaldir$runname/logs/

# Copy parameter file
cp -i -n  -v $paramfile $finaldir$runname/logs/

exit
