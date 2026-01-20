# Write a program which accept one number and check whether it is palindrome or not.

#input:121 Output:Palindrome

def Palindrome(no):
    temp=no
    rev=0

    while no > 0:
        digit= no % 10          # get last digit
        rev=rev * 10 + digit
        no= no // 10            # reverse last digit
    
    if rev == temp:
        print("It is palindrome")
    else:
        print("It is not palindrome")    

def main():
    print("Enter the number.")
    no=int(input())

    Palindrome(no)

if __name__ == "__main__":
    main()
