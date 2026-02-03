# Count Words in a File: Problem Statement: Write a program which accepts a file name from the user and 
# counts total number of words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.

def main():
    fileName=input("Enter the file name : ")
    
    try:
        fobj=open(fileName,"r")
        data=fobj.read()
        fobj.close()

        word=data.split()
        count=len(word)

        print("Total Word count is : ",count)

    except FileNotFoundError:
        print("Invalid file name.")

if __name__ == "__main__":
    main()