# Write a program which accepts one number from user and return its factorial.
# Input: 5
# Output: 120

def fact(no):
    fact=1
    for i in range(1,no+1,1):
        fact=fact * i
    return fact    

def main():
    print("Enter the number : ")
    no=int(input())

    result=fact(no)
    print("The Factorial of a number is : ",result)

if __name__ == "__main__":
    main()