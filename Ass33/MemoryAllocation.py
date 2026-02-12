# Add Actual Memory Allocation Feature: Display real memory usage of each process:
# RSS (Resident Set Size – actual RAM used)
# VMS (Virtual Memory)
# Memory Percentage

# Requirement: Show: Top 10 memory consuming processes

import sys
import time
import psutil
import schedule

def createLog(fileName):
    border="_"*50
    timeStamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName=fileName + "_" + timeStamp + ".log"

    print("Log file created : ",fileName)

    fobj=open(fileName,"w")

    process_data=[]

    for proc in psutil.process_iter(['pid','name','memory_info','memory_percent']):
        rss=proc.info['memory_info'].rss / (1024 * 1024)
        vms = proc.info['memory_info'].vms / (1024 * 1024)   # MB
        mem_per = proc.info['memory_percent']

        process_data.append([
            proc.info['name'],
            proc.info['pid'],
            rss,
            vms,
            mem_per
        ])

    # sort by memory percent
    process_data.sort(key=lambda x:x[4],reverse=True)

    top10=process_data[:10]

    fobj.write(border + "\n")
    fobj.write("---------- Memory Allocation Report ----------\n")
    fobj.write("Log Time : "+ time.ctime() + "\n")
    fobj.write(border + "\n\n")

    for p in top10:
        fobj.write("Process Name : " + str(p[0]) + "\n")
        fobj.write("PID          : " + str(p[1]) + "\n")
        fobj.write("RSS (MB)     : %.2f\n" % p[2])
        fobj.write("VMS (MB)     : %.2f\n" % p[3])
        fobj.write("Memory %%     : %.2f\n" % p[4])
        fobj.write(border + "\n")

    fobj.write("----------- End of Report -----------\n")
    fobj.write(border + "\n")

    fobj.close()

def main():
    border="_"*50
    print(border)
    print("---------- Memory Allocation Feature ----------")
    print(border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as:")
            print("ScriptName.py TimeInterval FileName")
            print("Time in minutes for periodic execution")

        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script displays memory allocation features:")

        else:
            print("Unable to process as no such option.")
            print("Please use --h or --u")

    elif len(sys.argv) == 3:
        print("Time interval : ",sys.argv[1])
        print("File name : ",sys.argv[2])

        schedule.every(int(sys.argv[1])).minute.do(createLog,sys.argv[2])

        print("Memory allocation started successfully.")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid number of arguments.")
        print("Please use --h or --u")

    print(border)
    print("--------- Thank you for using our script ---------")
    print(border)

if __name__ == "__main__":
    main()