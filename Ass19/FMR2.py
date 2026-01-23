# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.

# List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.**

# Input List : [5, 2, 3, 4, 3, 1, 2, 8, 10]

# List after filter : [2, 4, 2, 8, 10]
# List after map : [4, 16, 4, 64, 100]
# Output of reduce : 204
from functools import reduce

even=lambda no : no % 2 == 0

sqr=lambda no : no * no

add=lambda a,b : a + b

def main():
    print("Enter how many number of elements : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for i in range(no):
        value=int(input())
        data.append(value)

    Fdata=list(filter(even,data))
    print("Filter Data is : ",Fdata)

    Mdata=list(map(sqr,Fdata))
    print("Afet increase the map data is : ",Mdata)

    Rdata=reduce(add,Mdata)
    print("Reduce data is : ",Rdata)
if __name__ == "__main__":
    main()