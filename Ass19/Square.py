# Write a program which contains one lambda function which accepts one parameter and returns power of two.

# Input : 4
# Output : 16

# Input : 6
# Output : 64
from functools import reduce

sqr=lambda no : 2 ** no

def main():
    print("Enter number : ")
    no=int(input())

    result=sqr(no)
    print("Power of a number is : ",result)



if __name__ == "__main__":
    main()