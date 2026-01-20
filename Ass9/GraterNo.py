# Write a program which contains one function chkGreater() that accept two numbers and print the greater number.

def chkGreater(no1,no2):
    if(no1 > no2):
        print("No1 is greater : ",no1)
    else:
        print("No2 is greater : ", no2)   


def main():

    print("Enter first number : ")
    no1=int(input())

    print("Enter second number : ")
    no2=int(input())

    chkGreater(no1,no2)

if __name__ == "__main__":
    main()