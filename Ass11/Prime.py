# Write a program which accept one number and check whether it is prime or not.

def Prime(no):
    if no <= 1:
        print("Prime number.")
        return
    
    for i in range(2,no):
        if(no % i == 0):
            print("Not prime number.")
            return
    print("Prime number.")


def main():
    print("Enter the number : ")
    no=int(input())

    Prime(no)

if __name__ == "__main__":
    main()