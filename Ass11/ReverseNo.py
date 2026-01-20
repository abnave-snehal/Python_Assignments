# Write a program which accept one number and print reverse of that number.

#input:123 Output:321

def reverseNo(no):
    rev=0

    while no > 0:
        digit= no % 10          # get last digit
        rev=rev * 10 + digit
        no= no // 10            # reverse last digit
    print(rev)

def main():
    print("Enter the number.")
    no=int(input())

    reverseNo(no)

if __name__ == "__main__":
    main()
