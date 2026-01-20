# Write a program which accepts one number and prints factorial of that number.

def Fact(val):
    fact=1
    for i in range(1,val+1):
       fact= fact * i
    return fact  

def main():
    print("Enter the number for factorial : ")
    no=int(input())
    value=Fact(no)

    print("Factorial of a number is : ",value)

if __name__ == "__main__":
    main()