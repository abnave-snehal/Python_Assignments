# Design automation script which accept directory name and 
# display checksum of all files.

# Usage : DirectoryChecksum.py "Demo"

# Demo is name of directory.

import sys
import os
import hashlib

def CalculateChecksum(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)
        if len(data) == 0:
            break
        hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def DirectoryCheckSum(dirName):
    for folderName,subFolder,fileName in os.walk(dirName):
        for fName in fileName:
            filePath=os.path.join(folderName,fName)

            checksum=CalculateChecksum(filePath)

            print(fName, " -> ", checksum)

def main():
    if len(sys.argv) !=2:
        print("Invlaid Argument Passed:")
        return
    
    dirName=sys.argv[1]

    if os.path.exists(dirName) == False:
        print("Directory is not exists.")

    if os.path.isdir(dirName) == False:
        print("It's not a Directory.")

    DirectoryCheckSum(dirName)
        
if __name__ == "__main__":
    main()
