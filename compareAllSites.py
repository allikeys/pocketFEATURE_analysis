import sys
import re
import os
import subprocess
from io import open

def main():
        allFiles = os.listdir('.')
        feature_files = []
        for filename in allFiles:
                if filename.endswith('.ff'):
                        feature_files.append(filename)

        for i in range(len(feature_files)):
                for j in range(len(feature_files)):
                        #if (i >= j):
                        outFile = 'out.tmp'
                        subprocess.run(["perl", "/home/users/allikeys/CompareTwoSites.pl", feature_files[i], feature_files[j], "/home/users/allikeys/PocketFEATURE/All1160Cavity.std", "/home/users/allikeys/PocketFEATURE/TcCutoff4Normalize.txt", outFile])
                        subprocess.run(["cat", outFile])
                        fileNameI = re.sub(r'\.ff', '', feature_files[i])
                        fileNameJ = re.sub(r'\.ff', '', feature_files[j])
                        alignFile = fileNameI + '_' + fileNameJ + '.align'
                        scoreFile = fileNameI + '_' + fileNameJ + '.score'
                        subprocess.run(["rm", alignFile])
                        subprocess.run(["rm", scoreFile])

if __name__ == "__main__":
        main()
