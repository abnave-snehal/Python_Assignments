# Write a program to accepts two numbers and print addition, subtraction, multiplication and division of a number

def Add(no1,no2):
    return no1 + no2

def Sub(no1,no2):
    return no1 - no2

def Mul(no1,no2):
    return no1 * no2

def Div(no1,no2):
    return no1 / no2

def main():
    print("Enter first number : ")
    no1=int(input())

    print("Enter second number : ")
    no2=int(input())

    print("Addition of two number is :",Add(no1,no2))
    print("Subtraction of two number is :",Sub(no1,no2))
    print("Multiplication of two number is :",Mul(no1,no2))
    print("Division of two number is :",Div(no1,no2))
    

if __name__ == "__main__":
    main()