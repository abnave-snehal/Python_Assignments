# Search a Word in File: Problem Statement: Write a program which accepts a file name and 
# a word from the user and checks whether that word is present in the file or not.

# Input
# Demo.txt  Marvellous

# Expected Output
# Display whether the word Marvellous is found in Demo.txt or not.

def main():
    fileName=input("Enter the file name : ")
    word=input("Enter the word to search from the file : ")
    try:
        fobj=open(fileName,"r")
        data=fobj.read()
        fobj.close()

        if word in data:
            print("The word is found.")
        else:
            print("The word is not found.")
    except FileNotFoundError:
        print("Invlaid file name.")

if __name__ == "__main__":
    main()