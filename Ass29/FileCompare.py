# Compare Two Files (Command Line)
# Problem Statement: Write a program which accepts two file names through command line arguments and
# compares the contents of both files.

# If both files contain the same contents → display Success
# Otherwise → display Failure

# Demo.txt Hello.txt
# Success OR Failure
import sys

def main():
    if len(sys.argv) !=3:
        print("Invalid arguments.")
        return
    try:
        file1=sys.argv[1]
        file2=sys.argv[2]

        f1=open(file1,"r")
        f2=open(file2,"r")

        data1=f1.read()
        data2=f2.read()

        f1.close()
        f2.close()

        if data1 == data2:
            print("Success")
        else:
            print("Fail")

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()