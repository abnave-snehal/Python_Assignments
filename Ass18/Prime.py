# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and passes each number to ChkPrime() function
# ChkPrime() function is part of a user defined module named MarvellousNum
# Name of the function from main python file should be ListPrime()
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 10 34 2 5 8
# Output: 54 (13 + 5 + 7 + 2 + 5)

from functools import reduce
import MarvellousNum

print("Inside Main : ",__name__)
add=lambda a,b : a + b

def ListPrime(data):
    Fdata=list(filter(MarvellousNum.chkPrime,data))
    return reduce(add,Fdata)

def main():
    print("Enter how many number: ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for i in range(no):
        value=int(input())
        data.append(value)
    
    

    result=ListPrime(data)
    print("Addition is : ",result)

if __name__ == "__main__":
    main()