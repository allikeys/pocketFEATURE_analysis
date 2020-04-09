#!/bin/bash 
#
#all commands that start with SBATCH contain commands that are just used by SLURM for scheduling  
#SBATCH -p rbaltman
#SBATCH --time=7-00
#SBATCH --qos=normal
#SBATCH --nodes=1
#SBATCH --mem=40000


ml python/3.6.1
ml perl
cpanm List::MoreUtils
python3 /scratch/users/allikeys/covid_19/TMPSSR2/internal_comparison/compareAllSites.py
