import os
import shutil

documentFolder = "/home/boing/Documents"
downloadFolder = "/home/boing/Downloads"

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

for dictType in os.listdir(documentFolder):
    if (dictType in folderExist):
        folderExist.remove(dictType)

os.chdir(documentFolder)
for key in list(fileTypes.keys()):
    for fileName in fileTypes[key]:
        shutil.move(fileName, os.path.abspath(key))
        