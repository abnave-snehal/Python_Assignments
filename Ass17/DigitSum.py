# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def chkDigit(no):
    total=0
    while no > 0:
        digit= no % 10
        total= total + digit
        no= no // 10
        
    print(total)

def main():
    print("Enter the number:")
    no=int(input())

    chkDigit(no)

if __name__ == "__main__":
    main()