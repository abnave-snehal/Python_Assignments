# Write a program which accepts one number from user and return addition of it's factors.
# Input: 12
# Output: 16 (1+2+3+4+6)

def fact(no):
    fact=0
    for i in range(1,no):
        if(no % i == 0):
            fact=fact + i
    return fact    

def main():
    print("Enter the number : ")
    no=int(input())

    result=fact(no)
    print("The Factorial of a number is : ",result)

if __name__ == "__main__":
    main()