# pocketFEATURE_analysis

## Step 1: Parse PDB to find Binding Pockets
    * PDB_parser.py -- print the lists for each protein
            REQUIRES: PDB_Files - folder containing all PDB files of interes
                      Note: all filenames must be 4 characters long and contain at least one letter and number    
            INPUT: ligand_list: File of all acceptable 3 letter ligand identifiers
                      ex:  ligand_list.txt
            OUTPUT: One List for each PDB file in PDB_Files (filename: PDB_list.txt - from run on scPDB database)
                    (PDB_ID	  Ligand_ID	  SubUnit Letter    Residue Number)
            
