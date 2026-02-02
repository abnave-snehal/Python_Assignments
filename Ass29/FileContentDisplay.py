# Display File Contents: Problem Statement:
# Write program which accepts file name from user, opens that file, and
# displays the entire contents on the console.

# Input: Demo.txt

# Expected Output: Display contents of Demo.txt on console.

import os

def main():
    fileName=input("Enter file name : ")
    ret=os.path.exists(fileName)
    try:
        if ret == False:
            print("File is not exists")
        else:
            print("File exists")

        fobj=open(fileName,"r")
        print("File gets successfully opened.")

        Data=fobj.read()

        print("File data is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open the file.")

    finally:
        print("End of the application.")

if __name__ == "__main__":
    main()