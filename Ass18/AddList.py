
# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

# Input :
# Number of elements : 6
# Input Elements : 13 5 45 7 4 56

# Output :
# 130

from functools import reduce

addList=lambda a,b: a + b

def main():

    print("Enter the numbers : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for _ in range(no):
        value=int(input())
        data.append(value)

    Rdata=reduce(addList,data)
    print("Addition of list elements are : ",Rdata)

if __name__ == "__main__":
    main()
