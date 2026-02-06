# Design automation script which accept directory name and 
# write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.

# Usage : DirectoryDuplicate.py "Demo"

# Demo is name of directory.

import os
import sys
import time
import hashlib

def CalculateChkSum(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    Buffer=fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(dirName):
    if os.path.exists(dirName) == False:
        print("The directory is not exists.")
        return

    if os.path.isdir(dirName) == False:
        print("It's not a directory.")
        return

    duplicate={}

    FileLog=open("Log.txt","w")

    for folderName,subFolder,FileName in os.walk(dirName):
        for fName in FileName:
            fName=os.path.join(folderName,fName)
            chkSum=CalculateChkSum(fName)

            if chkSum in duplicate:
                duplicate[chkSum].append(fName)
            else:
                duplicate[chkSum]=[fName]

    for value in duplicate:
        if len(duplicate[value]) > 1:
            FileLog.write("Duplicate Files:\n")
            for fName in duplicate[value]:
                FileLog.write(fName + "\n")
            FileLog.write("\n")

    FileLog.close()
    print("Log.txt file created with the duplicate file name.")

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        return
    
    dirName=sys.argv[1]

    FindDuplicate(dirName)
    
if __name__ == "__main__":
    main()