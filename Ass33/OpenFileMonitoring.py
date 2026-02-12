import sys
import schedule
import time
import psutil


def createLog(fileName):

    border = "_" * 50
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = fileName + "_" + timeStamp + ".log"

    print("Log file created :", fileName)

    fobj = open(fileName, "w")

    fobj.write(border + "\n")
    fobj.write("------ Open File Monitoring Report ------\n")
    fobj.write("Log Time : " + time.ctime() + "\n")
    fobj.write(border + "\n\n")

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name']
            pid = proc.info['pid']

            try:
                files = proc.open_files()
                count = len(files)

            except psutil.AccessDenied:
                count = "Access Denied"

            fobj.write("Process Name : " + str(pname) + "\n")
            fobj.write("PID          : " + str(pid) + "\n")
            fobj.write("Open files   : " + str(count) + "\n")
            fobj.write(border + "\n")

        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            continue

    fobj.write("---------- End of report ----------\n")
    fobj.write(border + "\n")

    fobj.close()


def main():

    border = "_" * 50
    print(border)
    print("---------- Open File Monitoring Features ----------")
    print(border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--u", "--U"):
            print("Use the automation script as:")
            print("ScriptName.py TimeInterval FileName")
            print("Time in minutes for periodic execution")

        elif sys.argv[1] in ("--h", "--H"):
            print("This script displays:")
            print("Number of files opened by each process")

        else:
            print("Unable to process as no such option.")
            print("Please use --h or --u")

    elif len(sys.argv) == 3:

        print("Time Interval :", sys.argv[1])
        print("File Name :", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(createLog, sys.argv[2])

        print("Monitoring started successfully")
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
