#!/bin/bash 
#
#SBATCH -p rbaltman
#SBATCH --time=36:00:00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=40000

# Notes: 
# --------------------------
# First Argument - PDB List (output of PDB_parser.py)
# 
# Replace '/home/users/allikeys/GenerateCavityPoint_Vectorize.pl' with path to 'GenerateCavityPoint_Vectorize.pl' script.

ml perl
cpanm List::MoreUtils
perl /home/users/allikeys/GenerateCavityPoint_Vectorize.pl $1 6A 
