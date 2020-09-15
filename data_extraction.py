"""
This script uncompresses the data from the tar files. 

***Few notes********
- The dataset is broken up into three compressed files.
This script accepts the file paths as command line arguments and uncompresses them

"""

import shutil
import tarfile
import os
# from pathlib import Path
import sys


transcript_0to2 = str(sys.argv[1])
transcript_3to5 = str(sys.argv[2])
transcript_6to7 = str(sys.argv[3])

def extract_from_gz(file_path):
  tar = tarfile.open(file_path, "r:gz")
  for member in tar.getmembers():
    transcript = tar.extract(member,path=".")

extract_from_gz(transcript_0to2)
extract_from_gz(transcript_3to5)
extract_from_gz(transcript_6to7)


