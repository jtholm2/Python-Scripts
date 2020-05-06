import os, shutil

print("what is the name of the file you are looking for?")
fileName = input()
for folderName, subfolders, filenames in os.walk('c:\\'):
    for file in filenames:
        if str(file).startswith(fileName):
            print("Your file is located at: " + os.getcwd())
