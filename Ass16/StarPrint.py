# Write a program which accepts a number from the user and prints that number of "*" on the screen.

# Input : 5
# Output : * * * * * *

def star(no):
    for i in range(1,no+1):
        print("*", end=" ")    # end=" " keeps printing on the same line with a space

def main():
    print("Enter the number : ")
    no=int(input())

    star(no)

if __name__ == "__main__":
    main()