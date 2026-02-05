# Design automation script which accept two directory names. 
# Copy all files from first directory into second directory. 
# Second directory should be created at run time.

# Usage :
# DirectoryCopy.py "Demo" "Temp"

# Demo is name of directory which is existing and contains files in it.
# We have to create new directory as Temp and copy all files from Demo to Temp.

import os
import sys
import time
import shutil

def CopyFiles(srcDir,destDir):
    timeStamp=time.ctime()

    LogFile="Program3%s.log"%(timeStamp)
    LogFile=LogFile.replace(" ","_")
    LogFile=LogFile.replace(":","_")

    fobj=open(LogFile,"w")
    print("Log file created : ",LogFile)

    if os.path.exists(destDir) == False:
        os.mkdir(destDir)
        print("Destination directory created : ")

    count=0

    for folderName,subFolder,fileName in os.walk(srcDir):
        for fName in fileName:
            srcPath=os.path.join(folderName,fName)
            destPath=os.path.join(destDir,fName)

            shutil.copy(srcPath,destPath)

    print("Copied : ",srcPath, " -> ",destPath)
    fobj.write("\n Total files copied : %d" % count)
    fobj.close()

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments : ")

    srcDir=sys.argv[1]
    destDir=sys.argv[2]

    if os.path.exists(srcDir)==False:
        print("Source directory not found")
        return

    CopyFiles(srcDir,destDir)

if __name__ == "__main__":
    main()