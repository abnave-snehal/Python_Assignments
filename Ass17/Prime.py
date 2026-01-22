# Write a program which accepts one number from user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number

def chkPrime(no):
    if no <= 1:
        print("It is Prime Number")

    for i in range(2,no):
        if(no % i == 0):
            print("It is not a Prime")
            return
        
    print("It is Prime Number")

def main():
    print("Enter the number : ")
    no=int(input())

    chkPrime(no)


if __name__ == "__main__":
    main()