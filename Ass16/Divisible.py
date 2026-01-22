# Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5, otherwise return False.

# Input : 8
# Output : False

# Input : 25
# Output : True

def div5(no):
    if (no % 5 == 0):
        print("True")
    else :
        print("False")

def main():
    print("Enter the number : ")
    no=int(input())

    div5(no)

if __name__ == "__main__":
    main()