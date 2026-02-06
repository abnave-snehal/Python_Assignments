# Design automation script which accept directory name and delete all duplicate 
# files from that directory. Write names of duplicate files from that directory 
# into log file named as Log.txt. Log.txt file should be created into current directory.

# Usage :
# DirectoryDuplicateRemoval.py "Demo"

# Demo is name of directory.
import sys
import hashlib
import os

def chekSum(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    buffer=fobj.read(1024)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(dirName):
    if os.path.exists(dirName) == False:
        print("The directory is not exists")
        return {}
    
    if os.path.isdir(dirName) == False:
        print("It's not a directory.")
        return {}
    
    duplicate={}

    for folderName,subFolder,fileName in os.walk(dirName):
        for fName in fileName:
            fullPath=os.path.join(folderName,fName)
            chkSum=chekSum(fullPath)

            if chkSum in duplicate:
                duplicate[chkSum].append(fullPath)
            else:
                duplicate[chkSum]=[fullPath]

    return duplicate

def DuplicateRemove(dirName):
    MyDict=FindDuplicate(dirName)

    result=list(filter(lambda x:len(x) > 1,MyDict.values()))

    LogFile=open("Duplicate.txt","w")

    count=0
    cnt=0

    for value in result:
        for subvalue in value:
            count=count + 1
            if(count > 1):
                print("Deleted File : ",subvalue)
                os.remove(subvalue)
                LogFile.write(subvalue + "\n")
                cnt=cnt+1
        count=0

    print("Total deleted files : ",cnt)

    LogFile.write("Total deleted file : %d" % cnt)
    LogFile.close()

def main():
    if len(sys.argv) !=2:
        print("Invalid number of arguments.")
        return
    
    dirName=sys.argv[1]

    DuplicateRemove(dirName)

if __name__ == "__main__":
    main()