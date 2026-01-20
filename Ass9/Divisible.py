# Write a program which accepts one number and check whether it is divisible by 3 and 5.

def divisible(val):
    if(val / 3 and val / 5):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")    

def main():

    print("Enter the number : ")
    no=int(input())
    
    divisible(no)

 

if __name__ == "__main__":
    main()
