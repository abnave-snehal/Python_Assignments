# Check File Exists in Current Directory
# Problem Statement: Write program which accepts file name from user and
# checks whether that file exists in the current directory or not.
# Input: Demo.txt
# Expected Output: Display whether Demo.txt exists or not.

import os

def main():
    fileName=input("Enter File Name : ")
    ret=os.path.exists(fileName)

    if ret == False:
        print("File is not exists.")

    else:
        print("File  exists.")

if __name__ == "__main__":
    main()