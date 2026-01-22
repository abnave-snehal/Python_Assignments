# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934
# Output : 7

def chkDigit(no):
    cnt=0
    while no > 0:
        no= no // 10
        cnt=cnt + 1
    print(cnt)

def main():
    print("Enter the number:")
    no=int(input())

    chkDigit(no)

if __name__ == "__main__":
    main()