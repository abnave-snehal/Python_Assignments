# Count Lines in a File: Problem Statement:
# Write a program which accepts a file name from the user and 
# counts how many lines are present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt

def main():
    fileName=input("Enter the file name : ")
    fobj=open(fileName,"r")

    count=0

    for line in fobj:
        count=count+1
    print("Total lines are : ",count)

if __name__ == "__main__":
    main()