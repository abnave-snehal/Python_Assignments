# Write a lambda function using reduce() which accepts a list of numbers and returns maximum number.

from functools import reduce

max= lambda a,b : a if (a > b) else b

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

    Rdata=reduce(max,data)

    print("Maximum number of list is : ",Rdata)

if __name__ == "__main__":
    main()