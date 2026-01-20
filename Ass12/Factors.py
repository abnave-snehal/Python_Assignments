# Write a program which accept one number and print its factors.
# Input:12 Output:1 2 3 4 6 12


def factors(no):
  for i in range(1,no+1):   # (1,13)
     if(no % i == 0):       # (12 % 1 == 0)    
        print(i)



def main():
    print("Enter the number.")
    no=int(input())
    factors(no)

if __name__ == "__main__":
    main()