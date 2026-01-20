# Write a program which accepts one number and prints sum of first N natural numbers.
# 1+2+3+4+5=15

def sumN(val):
    sum=0

    for i in range(1,val+1):
        sum=sum + i
        i=i+1
    return sum

def main():

    print("Enter the number : ")
    no=int(input())

    result=sumN(no)

    print("The sum of N is : ",result)

if __name__ == "__main__":
    main()