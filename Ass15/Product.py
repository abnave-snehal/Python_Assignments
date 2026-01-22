# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

product= lambda a,b : a * b

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

    Rdata=reduce(product,data)

    print("Product of the elements are : ",Rdata)

if __name__ == "__main__":
    main()