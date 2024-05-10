import os
import shutil
import subprocess

name = subprocess.check_output('whoami').decode('utf-8').strip()
documentFolder = f"/home/{name}/Documents"
downloadFolder = f"/home/{name}/Downloads"

fileTypes = {}
folderExist = []

os.chdir(downloadFolder)
for file in os.listdir(downloadFolder):
    filename, extension = os.path.splitext(file)
    extension = extension.replace(".", "")
    if extension not in fileTypes:
        fileTypes[extension] = [] 
    fileTypes[extension].append(os.path.abspath(file))


if (fileTypes.keys() == None):
    SystemExit
  
folderExist = list(fileTypes.keys())
print(folderExist)
for dictType in os.listdir(documentFolder):
    if (dictType in folderExist):
        folderExist.remove(dictType)


os.chdir(documentFolder)
if (folderExist is not None):
    for dictName in folderExist:
        os.mkdir(dictName)

for key in list(fileTypes.keys()):
    for fileName in fileTypes[key]:
        shutil.move(fileName, os.path.abspath(key))
        
