# Write a program which contains one function named as ChkNum() which accepts one parameter as number.
# If the number is even then it should display "Even number" otherwise display "Odd number" on console.

# Input : 11
# Output : Odd Number

def chkNum(no):
    if(no % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter the number : ")
    no=int(input())

    chkNum(no)

if __name__ == "__main__":
    main()