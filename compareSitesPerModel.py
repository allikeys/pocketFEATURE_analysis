import sys
import re
import os
import subprocess
from io import open

def main(modelFile):
	#cfile = modelFile.replace('covidFiles/', '')
	
	cfile = modelFile.split('/')[-1]
	
	subprocess.run(["echo", cfile])
	outfile = 'out_' + cfile.replace('.ff', '') + '.tmp'
	subprocess.run(["touch", outfile])

	allFiles = os.listdir('/scratch/users/allikeys/covid_19/fFiles')
	feature_files = []
	for filename in allFiles:
		if filename.endswith('.ff'):
			feature_files.append(filename)

	
	for rfile in feature_files:
		subprocess.run(["perl", "/home/users/allikeys/CompareTwoSites.pl", rfile, cfile, "/home/users/allikeys/PocketFEATURE/All1160Cavity.std", "/home/users/allikeys/PocketFEATURE/TcCutoff4Normalize.txt", outfile])
		subprocess.run(["cat", outfile])
		fileNameR = re.sub(r'\.ff', '', rfile)
		fileNameC = re.sub(r'\.ff', '', cfile)
		alignFile = fileNameR + '_' + fileNameC + '.align'
		scoreFile = fileNameR + '_' + fileNameC + '.score'
		subprocess.run(["rm", alignFile])
		subprocess.run(["rm", scoreFile])


if __name__ == "__main__":
	main(sys.argv[1])
