# Write a program which accept one number and check whether it is perfect or not.
# Input: 6 Output: Perfect Number

def perfect(val):
    sum=0
    for i in range(1,val):
        if(val % i ==0):
            sum=sum + i    
    if(sum == val):
        print("It is perfect number : ",val)
    else:
        print("It is not a perfect number : ", val)         


def main():
    print("Enter the number : ")
    no=int(input())

    perfect(no)

if __name__ =="__main__":
    main()