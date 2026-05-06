#!/bin/bash

#get the env variable for the base_dir
base_dir=$GULLS_BASE_DIR
input_dir=$GULLS_INPUT_DIR
stars_dir=$GULLS_STARS_DIR
planets_dir=$GULLS_PLANETS_DIR
echo base_dir ${base_dir}
echo input_dir ${input_dir}
echo stars_dir ${stars_dir}
echo planets_dir ${planets_dir}

# the name of the paramfile is an arguement
pfile=$paramfile
if [ -z ${paramfile+x} ] && [ $# -ge 1 ]; then
    pfile=$1
elif [ -z ${paramfile+x} ] && [ $# -lt 1 ]; then
  echo "Usage:"
  echo "   $0 <parameterFile>"
  exit 1
fi
echo pfile ${pfile}

# right now defaulting to have a parameterFiles dir in base_dir, may not be the best but working withit for now
param_file_dir="parameterFiles/"

#test exit
paramfile=''
if [ -e $pfile ]; then
    paramfile=$pfile
elif [ -e $base_dir$param_file_dir$pfile ]; then
    paramfile=$base_dir$param_file_dir$pfile
else
  echo "Parameter file '$base_dir$param_file_dir$pfile' or '$pfile' not found"
  exit
fi

echo paramfile $paramfile

########################################################################
#    Less commonly changed options
########################################################################

#General options:
#GENERAL STRUCTURE: grep VAR_NAME in the base_dir/param_file_dir/paramfile

# all of these varaibles are path dependent (or better grouped here), so we give them paths
lensdir=$stars_dir`grep LENS_DIR $paramfile | awk -v FS='=' '{print $2}'`
lenslist=`grep LENS_LIST $paramfile | awk -v FS='=' '{print $2}'`
srcdir=$stars_dir`grep SOURCE_DIR $paramfile | awk -v FS='=' '{print $2}'`
srclist=`grep SOURCE_LIST $paramfile | awk -v FS='=' '{print $2}'`
sfdir=$stars_dir`grep STARFIELD_DIR $paramfile | awk -v FS='=' '{print $2}'`
sflist=`grep STARFIELD_LIST $paramfile | awk -v FS='=' '{print $2}'`
planetdir=$planets_dir`grep PLANET_DIR $paramfile | awk -v FS='=' '{print $2}'`
planetroot=`grep PLANET_ROOT $paramfile | awk -v FS='=' '{print $2}'`
obsdir=$input_dir`grep OBSERVATORY_DIR $paramfile | awk -v FS='=' '{print $2}'`
obslist=$obsdir`grep OBSERVATORY_LIST $paramfile | awk -v FS='=' '{print $2}'`
weatherdir=$input_dir`grep WEATHER_PROFILE_DIR $paramfile | awk -v FS='=' '{print $2}'`


#these varaibles have no path dependence, so they just get read in from the paramfile
#the output and final directory are independent of the location of this file tree
runname=`grep RUN_NAME $paramfile | awk -v FS='=' '{print $2}'`
outputdir=`grep OUTPUT_DIR $paramfile | awk -v FS='=' '{print $2}'`
#finaldir expects full path in parameterfile

finaldir=`grep FINAL_DIR $paramfile | awk -v FS='=' '{print $2}'`
subrunsize=`grep SUBRUNSIZE $paramfile | awk -v FS='=' '{print $2}'`
nsubruns=`grep NSUBRUNS $paramfile | awk -v FS='=' '{print $2}'`
simlength=`grep SIMULATION_LENGTH $paramfile | awk -v FS='=' '{print $2}'` #Length of time over which events could occur in the sim in years
    #(Not the length of the data collection)

#XXX see how this is used, may need a path before depsnding on how it is called later
executable=`grep EXECUTABLE $paramfile | awk -v FS='=' '{print $2}'`
WAITTIME=`grep MAXTIME $paramfile | awk -v FS='=' '{print $2}'`
OUTPUTLC=`grep OUTPUT_LC $paramfile | awk -v FS='=' '{print $2}'`
OUTPUTIMAGES=`grep OUTPUT_IMAGES $paramfile | awk -v FS='=' '{print $2}'`





########################################################################
#    Conventions
########################################################################

#Listed are the conventions the gulls pipeline relies on in order to 
#run successfully. Changes to these could require changes to the
#pipeline scripts, the underlying simulation code and the analysis
#scripts

###  The results and logs of each simulation are stored in a directory
#    named <outputdir>/<runname>/raw

###  The scripts used to run each sub-run, and their stdout and stderr
#    output are put in the directory <outputdir>/<runname>/logs

###  Files associated with the analysis of runs will be placed in
#    the <outputdir>/<runname>/analysis directory

###  The output files of each sub-run are named 
#    <runname>_<subRunNo>.out and <runname>_<subRunNo>.log
#    Both files are necessary for subsequent analysis. The files in 
#    the logs/ directory are not needed for analysis.

###  The lightcurves, and any subsequent analysis files, are stored in 
#    the outputdir/runname/lc directory, and are named
#    lc_<runname>_<subRunNo>_<idNo>.txt

###  The gulls pipeline scripts only take one argument, any other
#    options should be passed via the parameter file. Each run should
#    have a separate parameter file.

###  A copy of the parameter file, observatory list and files and 
#    weather files will be copied to the output files for future 
#    reference.

###  The SYNTHGALROOT option in the parameter file is expected to
#    end with a dot. i.e. gal_H_0.dat.

###  The gulls simulator is launched as
#    ./gulls -i <parameterFile> -s <subRunNo>

###  If you have a short user name, you may have to adapt the scripts 
#    to reliably select only jobs you have submitted from the qstat 
#    running jobs list

###  Directories are listed in the parameter file with their trailing
#    slash. In fact any variable that holds a directory, and whos 
#    name ends in dir or DIR, will include the trailing slash

### Runname must be 10 characters or less, and must not contain an
#   underscore
