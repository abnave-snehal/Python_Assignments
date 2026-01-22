# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

div= lambda no : (no % 3 == 0) and (no % 5 == 0)

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

    Fdata=list(filter(div,data))

    print("Divisible by 3 and 5 : ",Fdata)

if __name__ == "__main__":
    main()