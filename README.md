# pocketFEATURE_analysis
    Requirements: 
        PocketFEATURE - download link: https://simtk.org/projects/pocketfeature
        DSSP executable 

## Step 1: Parse PDB Files to find Binding Pockets
    PDB_parser.py -- print the lists for each protein
            REQUIRES: 
                A folder containing all PDB files of interest
                    Note: all filenames must be 4 characters long and contain at least one letter and number    
            INPUTS: 
                ligand_list: File of all acceptable 3 letter ligand identifiers (i.e. ligand_list.txt)
                path: Path to folder containing PDB Files
                outfile: Name of desired ouput file (i.e. PDB_list.txt)
            OUTPUT: 
                A file witha  line for each valid protein, ligand pair in the PDB Files directory of format:
                    PDB_ID	  Ligand_ID	  SubUnit Letter    Residue Number
                    
## Step 2: Run DSSP on all PDB Files
    runDSSP.sh -- Runs DSSP executable (dssp-2.0.4-linux-i38) on all PDB files in specified folder
               -- Creates a corresponding .dssp file for each .pdb file. 
        REQUIRES: 
            A folder containing all PDB files of interest
        INPUTS:  
            path: Path to folder containing PDB Files
            
## Step 3: Generate Cavity Points 
    GenerateCavity.sh -- Generates the pocket desciptor files for all pockets described in the PDB_list. 
                      -- ex. files: 1pdb_LIG.dssp, 1pdb_LIG.ff, 1pdb_LIG.lig, 1pdb_LIG.pdb, 1pdb_LIG.ptf
        REQUIRES:
            A folder containing all PDB files and their corresponding dssp files (ex: 1pdb.pdb, 1pdb.dssp)
            GenerateCavityPoint_Vectorize.pl - script from pocketFEATURE
            Note: Should be run in folder with .dssp and .pdb files. 
        INPUTS: 
            pdb_list: List of pockets output by PDB_parser.py
            
## Step 4: Compare Pockets

### Option 1: Compare all pockets against a specific short list of pockets
    perModelSubmission.sh -- Submits one batch script to compare all feature files in the main directory against feature files in a given subdirectory
        REQUIRES:
            Submission script must be in the folder containing all feature files (.ff) of interest
            Sub-folder with feature files for short list of pockets to be compared against full list must be in main folder
            compareSitesPerModel.sh - Submission script to call python script with appropriate pocket
            compareSitesPerModel.py - Python script to run all individual comparisons
            CompareTwoSites.pl - Script from PocketFEATURE to compare a given pair of pockets
            Note: Ensure that the locations of the two required scripts are fixed for your system in the other scripts
        INPUTS:
            path: The path to the sub-folder of interest
        OUTPUT:
            one slurm file per pocket on the short list of pockets containing the scores comparing a single pocket to all others

### Option 2: Compare all pockets against all other pockets
    compareAllSubmission.sh -- 
        REQUIRES:
            Submission script must be in the folder containing all feature files (.ff) of interest
            compareAllSites.py - Python script to make comparisons between all feature files in given folder
            CompareTwoSites.pl - Script from PocketFEATURE to compare a given pair of pockets
            Note: Ensure that the locations of the two required scripts are fixed for your system in the other scripts
        INPUTS: 
            None
        OUTPUT:
            A single slurm file containing all pairwise comparison scores. 
            
