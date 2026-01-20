# Write a program which accepts one number and prints cube of that number.

def cube(no):
    ret=0

    ret=no * no * no
    return ret

def main():

    print("Enter number for cube : ")
    no=int(input())

    result=cube(no)
    print("The cube of a given number is : ",result)

if __name__ == "__main__":
    main()