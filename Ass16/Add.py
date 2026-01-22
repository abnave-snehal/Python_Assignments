# Write a program which contains one function named as ChkNum() which accepts one parameter as number.
# If the number is even then it should display "Even number" otherwise display "Odd number" on console.

# Input : 11 5
# Output : 16

def Add(no1,no2):
   sum=0
   sum= no1 + no2
   return sum 

def main():
    no1=int(input("Enter first number : "))
    no2=int(input("Enter second number : "))

    ret=Add(no1,no2)

    print("Addition of two numbers is :",ret)

if __name__ == "__main__":
    main()