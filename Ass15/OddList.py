# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd number.

odd= lambda no : no % 2 == 1

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

    Fdata=list(filter(odd,data))    

    print("Odd of a element is : ",Fdata)

if __name__ == "__main__":
    main()