# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# * * * * *
# * * * *
# * * *
# * *
# *

def starPrint(no):
    for i in range(1,no+1,1):
        print(" ".join(['*'] * (no - i + 1)))   # Join '*' with space and repeat no times 

def main():
    print("Enter the number : ")
    no=int(input())

    starPrint(no)

if __name__ == "__main__":
    main()