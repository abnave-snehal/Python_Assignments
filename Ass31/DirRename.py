# Design automation script which accept directory name and 2 file extensions from user.
# Rename all files with first file extension with the second file extension.

# Usage : DirectoryRename.py "Demo" ".txt" ".doc"

# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.
import os
import time
import sys

def dirReanme(folderName,oldExt,newExt):
    timeStamp=time.ctime()

    LogFileName="Program2%s.log" %(timeStamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    fobj=open(LogFileName,"w")
    print("Log File Created : ",LogFileName)

    count=0

    for folderName,subFolder,fileName in os.walk(folderName):
        for fName in fileName:
            if fName.lower().endswith(oldExt.lower()):
                oldPath=os.path.join(folderName,fName)

                newName=fName[:-len(oldExt)] + newExt
                newPath=os.path.join(folderName,newName)

                os.rename(oldPath,newPath)

                print("Renamed : ",oldPath, "->",newPath)
                fobj.write(oldPath+ " -> " +newPath+ "\n")

                count+=1

    print("Total file renamed:",count)
    fobj.write("\n Total file renamed : %d" % count)

    fobj.close()

    if os.path.exists(folderName) == False:
        print("Directory not found:")

    if os.path.isdir(folderName) == False:
        print("It's not a directory:")
    
    LogFileName="Rename"



def main():
    if (len(sys.argv) != 4):
        print("Invalid Number of arguments : ")

    folderName=sys.argv[1]
    oldExt=sys.argv[2]
    newExt=sys.argv[3]

    dirReanme(folderName,oldExt,newExt)

if __name__ == "__main__":
    main()