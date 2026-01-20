# Write a program which accept one number and print sum of digint.

#input:123 Output:6

def digitSum(no):
    total=0

    while no > 0:
        digit= no % 10          # get last digit
        total=total + digit
        no= no // 10            # remove last digit
    print(total)

def main():
    print("Enter the number.")
    no=int(input())

    digitSum(no)

if __name__ == "__main__":
    main()
