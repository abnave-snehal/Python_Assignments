# Display File Line by Line: 
# Problem Statement: Write a program which accepts a file name from the user
# and displays the contents of the file line by line on the screen.

# Input
# Demo.txt

# Expected Output
# Display each line of Demo.txt one by one.

def main():
    fileName=input("Enter the file name : ")
    try:
        fobj=open(fileName,"r")

        for line in fobj:
            print(line, end="")

        fobj.close()

    except FileNotFoundError:
        print("Invalid file name.")

if __name__ == "__main__":
    main()