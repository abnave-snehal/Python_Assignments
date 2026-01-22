# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

sqr= lambda no : no * no

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

    Mdata=list(map(sqr,data))    

    print("Square of a element is : ",Mdata)

if __name__ == "__main__":
    main()