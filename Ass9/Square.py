# Write a program which accepts one number and prints square of that number.

def square(no):
    ret=0

    ret=no * no
    return ret

def main():

    print("Enter number for square root : ")
    no=int(input())

    result=square(no)
    print("The square root of a given number is : ",result)

if __name__ == "__main__":
    main()