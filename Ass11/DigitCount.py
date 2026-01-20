# Write a program which accept one number and print count of digint in that number.

#input:7521 Output:4

def digitCount(no):
    count=0

    while no > 0:
        no = no // 10
        count= count + 1
    print(count)


def main():
    print("Enter the number.")
    no=int(input())

    digitCount(no)

if __name__ == "__main__":
    main()
