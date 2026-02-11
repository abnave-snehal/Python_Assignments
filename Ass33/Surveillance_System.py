# Add Thread Monitoring Feature: For each running process, display:
# Process Name, PID, Number of Threads created by that process
#  Requirement:
# Store information in log file along with timestamp.

import sys
import schedule
import time
import os
import psutil

def CreatLog(FileName):
    border="_"*50

    timeStamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=FileName + "_" + timeStamp + ".log"

    print("LogFile is created : ",FileName)

    fobj=open(FileName,"w")

    fobj.write(border+"\n")
    fobj.write("---------- Platform Survillance System ----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(border+"\n\n")

    for proc in psutil.process_iter(['pid','name','num_threads']):
        try:
            pname=proc.info['name']
            pid=proc.info['pid']
            threads=proc.info['num_threads']

            fobj.write("---------- System Report ----------\n")
            fobj.write("Process Name : " + str(pname) + "\n")
            fobj.write("Process ID(PID) : " + str(pid) + "\n")
            fobj.write("Number of thread created by that process : " + str(threads) + "\n\n")
            fobj.write(border + "\n")
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    fobj.close()

def main():
    border="_"*50
    print(border)
    print("---------- Platform Survillance System ----------")
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to Display:")
            print("Process Name ")
            print("Process ID")
            print("Number of thread created by that process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as:")
            print("ScriptName.py TimeInterval FileName.")
            print("Time in a minutes for periodic execution.")
            print("FileName to show the information stored init.")
        
        else:
            print("Unable to process as no such option.")
            print("Please use --h or --u for more details.")
    
    elif(len(sys.argv) == 3):
        print("Time Interval : ",sys.argv[1])
        print("File Name: ",sys.argv[2])

        # Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreatLog,sys.argv[2])

        print("Platform system survillance system started successfully.")
        print("File Name created with the :",sys.argv[2])
        print("Time interval in a  minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments.")
        print("Please use --h or --u for more details.")

    print(border)
    print("--------- Thank you for using our script ---------")
    print(border)

if __name__ == "__main__":
    main()