# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10.
# Reduce will return product of all that numbers.**

# Input List : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter : [76, 89, 86, 90, 70]
# List after map : [86, 99, 96, 100, 80]
# Output of reduce : 6538752000
from functools import reduce

chkRange=lambda no : no >= 70  and no <= 90

increase=lambda no : no + 10

product=lambda a,b : a * b

def main():
    print("Enter how many number of elements : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for i in range(no):
        value=int(input())
        data.append(value)

    Fdata=list(filter(chkRange,data))
    print("Filter Data is : ",Fdata)

    Mdata=list(map(increase,Fdata))
    print("Afet increase the map data is : ",Mdata)

    Rdata=reduce(product,Mdata)
    print("Product of the elements is : ",Rdata)
if __name__ == "__main__":
    main()