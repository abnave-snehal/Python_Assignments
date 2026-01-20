# Write a program which accept one number and print all even numbers till that number.

def EvenN(no):
    for i in range(1,no+1):
        if (i % 2 == 0):
            print(i)

def main():
    print("Enter the number : ")
    no=int(input())

    EvenN(no)
  
if __name__ == "__main__":
    main()