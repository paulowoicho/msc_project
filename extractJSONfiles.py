import json
import shutil
import tarfile
import os

entries = [] #list with the json filenames

i=0
tar = tarfile.open("C:\\Users\\Owoicho\\Desktop\\Dissertation\\dataset\\podcasts-transcripts-6to7.tar.gz", "r:gz")

for member in tar.getmembers():
    i+=1
    if i<=100:
        f = tar.extract(member,path=".")
    else:
        break

# for member in tar.getmembers():
#     while i <= 100:
#         f = tar.extract(member, path='.')
#         i += 100

    
tar.close()
