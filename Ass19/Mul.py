# 2. Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

# Input : 4 3
# Output : 12

# Input : 6 3
# Output : 18

mul=lambda a,b : a * b

def main():
    no1=int(input("Enter first number : "))
    no2=int(input("Enter second number : "))

    result=mul(no1,no2)
    print("Multiplication of two number is : ",result)


if __name__ == "__main__":
    main()