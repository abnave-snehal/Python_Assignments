# Copy File Contents into a New File (Command Line) : Problem Statement:
# Write a program which accepts an existing file name through command line arguments,
# creates a new file named Demo.txt, and copies all contents into Demo.txt.

# Input (Command Line): ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.
import sys

def main():
    if len(sys.argv) != 2:
        print("Invalid number of command line arguments: ")
        return
    
    try:
        source=sys.argv[1]
        destination="Demo.txt"

        fobj=open(source,"r")
        data=fobj.read()
        fobj.close()

        newf=open(destination,"w")
        newf.write(data)
        newf.close()

        print("File gets copied into Demo.txt")

    except FileNotFoundError:
        print("File is not present.")

if __name__ == "__main__":
    main()