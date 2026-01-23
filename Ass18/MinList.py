
# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

# Input :
# Number of elements : 4
# Input Elements : 13 5 45 7

# Output :
# 5
from functools import reduce

minList=lambda a,b: a if (a < b) else b

def main():
    print("Enter the numbers : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for _ in range(no):
        value=int(input())
        data.append(value)

    Rdata=reduce(minList,data)
    print("Minimum number from list is : ",Rdata)

if __name__ == "__main__":
    main()
