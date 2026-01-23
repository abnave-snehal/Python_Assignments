
# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

# Input :
# Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34

# Output :
# 56
from functools import reduce

maxList=lambda a,b: a if (a > b) else b

def main():
    print("Enter the numbers : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for _ in range(no):
        value=int(input())
        data.append(value)

    Rdata=reduce(maxList,data)
    print("Maximum number from list is : ",Rdata)

if __name__ == "__main__":
    main()
