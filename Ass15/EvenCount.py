# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

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

    print("Even count of a number is : ",len(Fdata))

if __name__ == "__main__":
    main()