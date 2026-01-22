# Write a lambda function using filter() which accepts a list of numbers and returns a list of even number.

even= lambda no : no % 2 == 0

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

    Fdata=list(filter(even,data))    

    print("Even of a element is : ",Fdata)

if __name__ == "__main__":
    main()