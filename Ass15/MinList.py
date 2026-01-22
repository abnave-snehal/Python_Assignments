# Write a lambda function using reduce() which accepts a list of numbers and returns minimum number.

from functools import reduce

min= lambda a,b : a if (a < b) else b

def main():
    size=0
    value=0

    print("Enter number of elements : ")
    no=int(input())

    data=list()
    print("Enter the elemnts to the list : ")
    for i in range(no):
        value=int(input())
        data.append(value)

    Rdata=reduce(min,data)

    print("Minimum number of list is : ",Rdata)

if __name__ == "__main__":
    main()