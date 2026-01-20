# Write a program which accepts one number and prints multiplication table of that number.

def Mul(val):
    for i in range(1,11):
        print(val*i)

def main():
    print("Enter the number for multiplication of a table : ")
    no=int(input())
    result=Mul(no)

if __name__ == "__main__":
    main()