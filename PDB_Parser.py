#Inputs:
#	ligand_file: List of approved ligands, one per line
# 	path: Path to directory with PDB Files
#	out_name: Name of the output file to create

import sys
import re
import os
from io import open
import pandas as pd

def getAllFiles(path):
	allFiles = os.listdir(path)
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
	if line[0:len('HETATM')] == 'HETATM':
		lig = line[17:20].lstrip()
		chain = line[21:22].lstrip()
		pos = line[22:28].lstrip()
		return [lig, chain, pos]

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

def main(ligandlist, path, out_name):

	outfile = open(out_name, "w")
	ligands = getLigands(ligandlist)
	pdb_files = getAllFiles(path)

	for pdb_file in pdb_files: 
		file = open(os.path.join(path, pdb_file), 'r')
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
	try: 
		ligandlist = sys.argv[1]
		path = sys.argv[2]
		out_name = sys.argv[3]
	except:
		print("Incorect Usage! Run with the following arguments: \n    Arg1 - ligand_file: List of approved ligands, one per line\n    Arg2 - path: Path to folder containing PDB Files\n    Arg3 - out_name: Name of the output file to create")
		sys.exit()
	main(ligandlist, path, out_name)
