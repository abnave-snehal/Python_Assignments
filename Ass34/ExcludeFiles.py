# Exclude Files/Folder: Ignore: 1).tmp 2).log 3).exe 4)Or user defined extensions


import os
import time
import shutil
import sys
import zipfile
import hashlib
import schedule

ignore_ext=[".exe",".tmp",".log"]

def shouldIgnore(fileName,userExt=None):
    if userExt is None:
        userExt=[]

    ext=os.path.splitext(fileName)[1].lower()

    if ext in ignore_ext or ext in userExt:
        return True
    
    return False

def restoreBackup(zipName,destination):
    if not os.path.exists(zipName):
        writeLog("ERROR: Zip file not found : " + zipName)
        return
    
    os.makedirs(destination,exist_ok=True)

    writeLog("Restore start at : " + time.ctime())
    writeLog("Zip File : " + zipName)
    writeLog("Destination : " + destination)

    zobj=zipfile.ZipFile(zipName,"r")

    for name in zobj.namelist():
        zobj.extract(name,destination)
        writeLog("Extracted : " + name)

    zobj.close()

    writeLog("Restore completed successfully")


def writeLog(message):
    os.makedirs("Logs",exist_ok=True)

    log_name=time.strftime("Logs/Backup_%Y-%m-%d.log")

    with open(log_name, "a") as fobj:
        fobj.write(message + "\n")

def makeZip(folder,userExt=None):
    timeStamp=time.strftime("%Y-%m-%d_%H-%M-%S")

    zipName=folder + "_" +timeStamp + ".zip"

    zobj=zipfile.ZipFile(zipName,"w",zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(folder):
        for file in files:

            if shouldIgnore(file,userExt):
                writeLog("Ignored File" + file)
                continue

            fullPath=os.path.join(root,file)
            relative=os.path.relpath(fullPath,folder)

            zobj.write(fullPath,relative)

    zobj.close()

    return zipName

def calculateHash(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    
    fobj.close()

    return hobj.hexdigest()

def backupFiles(source,destination):
    copiedFiles=[]

    print("Creating the backup folder for backup process : ")

    os.makedirs(destination,exist_ok=True)

    for root,dirs,files in os.walk(source):
        for file in files:
            if shouldIgnore(file):
                writeLog("Ignored File " + file)
                continue
            
            srcPath=os.path.join(root,file)

            relative=os.path.relpath(srcPath,source)

            desPath=os.path.join(destination,relative)

            os.makedirs(os.path.dirname(desPath),exist_ok=True)

            if((not os.path.exists(desPath) or (calculateHash(srcPath) != calculateHash(desPath)))):
                shutil.copy2(srcPath,desPath)
                copiedFiles.append(relative)

    return copiedFiles

def marvellousDataShildStart(source="Data"):
    border="_"*50

    backupName="MarvellousBackup"

    print(border)
    print("Backup process started successfully : ",time.ctime())
    print(border)

    files=backupFiles(source,backupName)

    zipfile=makeZip(backupName)

    print(border)
    print("Backup completed successfully.")
    print(border)
    print("File copied :",len(files))
    print("Zip file gets created : ",zipfile)
    print(border)

def main():
    border="_"*50
    print(border)
    print("---------- Data Shild System ----------")
    print(border)

    if(len(sys.argv) == 4) and sys.argv[1] == "--restore":
        zipfile=sys.argv[2]
        dest=sys.argv[3]

        restoreBackup(zipfile,dest)

        return

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv) == 3):
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(marvellousDataShildStart, sys.argv[2])

        print(border)
        print("Data Sheild System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(border)

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(border)
    print("--------- Thank you for using our script ---------")
    print(border)
    
if __name__ == "__main__":
    main()