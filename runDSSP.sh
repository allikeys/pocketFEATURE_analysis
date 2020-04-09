#!/bin/sh
#
#SBATCH -p rbaltman
#SBATCH --time=01:30:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=40000

# Notes:
# -------------------------
# PATH - The path to all pdb files to dssp - i.e. 'Protease/PDB_Files/*'
# replace '/scratch/users/allikeys/covid_19/dssp-2.0.4-linux-i386' with path to dssp executable. 

PATH=$1
FILES=$PATH/*

for i in $FILES; do
/scratch/users/allikeys/covid_19/dssp-2.0.4-linux-i386 -i $i -o ${i%.pdb}.dssp
done
