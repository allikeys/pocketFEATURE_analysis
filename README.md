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
    compareSitesPerModel.sh -- 
        REQUIRES:
            compareSitesPerModel.py -
            

### Option 2: Compare all pockets against all other pockets
    compareAllSites.sh -- 
        REQUIRES:
            compareAllSites.py - python script to make comparisons between 
            
            
            
