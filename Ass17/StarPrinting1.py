# Write a program which accepts one number and displays the below pattern.
# Input: 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def starPrint(no):
    for i in range(1,no+1,1):
        print(" ".join(['*'] * no))   # Join '*' with space and repeat no times 

def main():
    print("Enter the number : ")
    no=int(input())

    starPrint(no)

if __name__ == "__main__":
    main()