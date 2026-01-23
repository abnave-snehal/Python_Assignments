# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return maximum number from that numbers.
# (You can also use normal functions instead of lambda functions.)
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def prime(no):
    if no <= 1:
        return False
    for i in range(2,no):
        if (no % i == 0):
            return False
    return True
       
mul=lambda no : no * 2

max=lambda a,b : a if (a > b) else b

def main():
    print("Enter how many number of elements : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for i in range(no):
        value=int(input())
        data.append(value)

    Fdata=list(filter(prime,data))
    print("Filter Data is : ",Fdata)

    Mdata=list(map(mul,Fdata))
    print("Map data is : ",Mdata)

    Rdata=reduce(max,Mdata)
    print("Reduce data is : ",Rdata)
if __name__ == "__main__":
    main()