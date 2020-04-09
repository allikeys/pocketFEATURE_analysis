#!/bin/bash
#
#SBATCH -p rbaltman
#SBATCH --time=7-00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=40000

#FileDir is path to model files to compare. i.e. "Protease"
FILEDIR=$1
FILES=$FILEDIR/*

for f in $FILES
do 
	echo $f
	sbatch /scratch/users/allikeys/covid_19/chloroquine_test/fFiles/compareSitesPerModel.sh $f
done

