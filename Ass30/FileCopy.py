# Copy File Contents into Another File:
# Problem Statement: Write a program which accepts two file names from the user:

# First file = existing file
# Second file = new file
# Copy all contents from first file into second file

# Input: ABC.txt XYZ.txt

# Expected Output: Content of ABC.txt copied into XYZ.txt

def main():
    file1=input("Enter first file : ")
    file2=input("Enter second file : ")
    try:
        f1obj=open(file1,"r")
        f2obj=open(file2,"w")

        data=f1obj.read()
        f2obj.write(data)
        print("Content of the file gets copied from ABC.txt to XYZ.txt : ")

        f1obj.close()
        f2obj.close()

    except FileNotFoundError:
        print("Invlaid file name.")

if __name__ == "__main__":
    main()