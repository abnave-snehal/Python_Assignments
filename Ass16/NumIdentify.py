# Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

# Input : 11
# Output : Positive Number

# Input : -8
# Output : Negative Number

# Input : 0
# Output : Zero

def numIdentify(no):
    if (no == 0):
        print("Zero")
    elif (no < 0):
        print("Negative Number")
    else :
        print("Positive number")

def main():
    print("Enter the number : ")
    no=int(input())

    numIdentify(no)

if __name__ == "__main__":
    main()