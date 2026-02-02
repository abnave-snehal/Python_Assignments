# Frequency of a String in File: Problem Statement
# Write a program which accepts a file name and one string from the user and 
# returns the frequency (count of occurrences) of that string in the file.

# Input: Demo.txt  Marvellous
# Expected Output: Count how many times "Marvellous" appears in Demo.txt

def main():
    fileName=input("Enter the file name : ")
    word=input("Enter the string : ")

    fobj=open(fileName,"r")
    data=fobj.read()
    fobj.close()

    wordCnt=data.count(word)
    
    print("Frequency of word is : ",wordCnt)

if __name__ == "__main__":
    main()