#Inputs:
#	ligand_file: List of approved ligands, one per line
#	out_name: Name of the output file to create

import sys
import re
import os
from io import open
import pandas as pd

def getAllFiles():
	allFiles = os.listdir('PDB_Files')
	pdb_files = []
	for filename in allFiles:
		if filename.endswith('.pdb'):
			pdb_files.append(filename)
	return pdb_files

def getLigands(ligand_file):
	ligand_list = open(ligand_file, 'r')
	ligand_lines = ligand_list.readlines()
	ligands = []
	for item in ligand_lines:
		ligands.append(str(item).strip())
	return ligands

def processLine(line):
	beginning = line[0:17]
	middle = [''] * 3

	if line[0:len('HETATM')] == 'HETATM':
		first_half = line[17:29].split()
		middle[0:len(first_half)] = first_half

		if len(middle[1]) > 1:
			middle[2] = middle[1][1:]
			middle[1] = middle[1][0:1]
		#print(middle)
		return middle

	return ''


def printOutput(df, ligands, pdb_id, outfile):
	used_ligands = []
	for i in df.index:
		lig = df.loc[i, 'Lig']	
		if (lig in ligands) and (lig not in used_ligands):
			out_str = pdb_id + '\t' + df.loc[i, 'Lig'] + '\t' + df.loc[i, 'Chain'] + '\t' + df.loc[i, 'Pos'] + '\n'
			outfile.write(out_str)
			#print(pdb_id + '\t' + df.loc[i, 'Lig'] + '\t' + df.loc[i, 'Chain'] + '\t' + df.loc[i, 'Pos'])
			used_ligands.append(lig)

def main(ligandlist, out_name):

	outfile = open(out_name, "w")
	ligands = getLigands(ligandlist)
	pdb_files = getAllFiles()

	for pdb_file in pdb_files:
		file = open(os.path.join('PDB_Files', pdb_file), 'r')
		pdb_id = pdb_file[:-4]
		hetatm_lines = []

		line = str(file.readline())
		while (line):
			if line.startswith('HETATM'):
				fixedLine = processLine(line)
				if len(fixedLine) == 3:
					hetatm_lines.append(fixedLine)
			line = str(file.readline())

		header = ['Lig', 'Chain', 'Pos']
		df = pd.DataFrame(hetatm_lines, columns=header)
		file.close()

		printOutput(df, ligands, pdb_id, outfile)
	outfile.close()
			
if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
