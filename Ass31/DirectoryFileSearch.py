# Design automation script which accept directory name and file extension from user.
# Display all files with that extension.

# Usage : DirectoryFileSearch.py "Demo" ".txt"

# Demo is name of directory and .txt is the extension that we want to search.

import os
import sys
import time

def DirSearch(dirName,fileExtension):
    timeStamp=time.ctime()
    LogFileName="Program1%s.log" %(timeStamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    fobj=open(LogFileName,"w")

    fobj.write("---------- Log file created ----------:")

    count=0

    for folderName,subFolder,fileName in os.walk(dirName):
        for fName in fileName:
            if fName.lower().endswith(fileExtension.lower()):
                FullPath=os.path.join(folderName,fName)
                print("Full Path is : ",FullPath)
                count+=1
    print("Total matching file count is : ",count)

    fobj.write("\n Total matching file count is : %d "% count)

def main():
    if len(sys.argv) !=3:
        print("The arguments should <Filename> <Foldername> <fileextension>.")
        return
    
    dirName=sys.argv[1]
    fileExtension=sys.argv[2]

    ret=os.path.exists(dirName)

    if (ret == False):
        print("There is no such directory:")

    ret=os.path.isdir(dirName)

    if(ret == False):
        print("It's not a directory:")

    DirSearch(dirName,fileExtension)

if __name__ == "__main__":
    main()
