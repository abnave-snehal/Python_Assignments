# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

strLen=lambda s : len(s) > 5

def main():
    value=0
    print("Enter the number : ")
    no=int(input())

    data=list()
    print("Enter the strings : ")
    for i in range(no):
        value=input()
        data.append(value)

    Fdata=list(filter(strLen,data))

    print("String length grater then 5 are : ",Fdata)

if __name__ == "__main__":
    main()