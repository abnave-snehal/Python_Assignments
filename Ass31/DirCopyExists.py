# Design automation script which accept two directory names and one file extension.
# Copy all files with the specified extension from first directory into second directory. 
# Second directory should be created at run time.

# Usage :
# DirectoryCopyExt.py "Demo" "Temp" ".exe"

# Demo is name of directory which is existing and contains files in it.
# We have to create new directory as Temp and copy all files with extension .exe from Demo to Temp.

import os
import sys
import time
import shutil

def dirCopyExists(dir1,dir2,fileExt):
    timeStamp=time.ctime()

    LogFile="Program4%s.log"%(timeStamp)
    LogFile=LogFile.replace(" ","_")
    LogFile=LogFile.replace(":","_")

    fobj=open(LogFile,"w")
    print("Log file is created : ",LogFile)

    if os.path.exists(dir2) == False:
        os.mkdir(dir2)
        print("Directory is created:")
    
    count=0

    for folderName,subFolder,fileName in os.walk(dir1):
        for fName in fileName:
            if fName.lower().endswith(fileExt.lower()):
                srcPath=os.path.join(folderName,fName)
                desPath=os.path.join(dir2,fName)

                shutil.copy(srcPath,desPath)

                print("Copied :",srcPath,"->",desPath)
                
                fobj.write(srcPath+"->"+desPath+"\n")

                count+=1

        print("Total files copied : ",count)
        fobj.write("\nTotal files copied : %d" % count)

        fobj.close()

def main():
    if len(sys.argv) !=4:
        print("Invalid number of arguments:")
        return

    dir1=sys.argv[1]
    dir2=sys.argv[2]
    fileExt=sys.argv[3]

    if os.path.exists(dir1) == False:
        print("The Directory is not exists:")
        return

    if os.path.isdir(dir1) == False:
        print("It's not a directory:")
        return

    dirCopyExists(dir1,dir2,fileExt)

if __name__ =="__main__":
    main()