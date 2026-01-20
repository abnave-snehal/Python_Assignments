# Write a program which accepts one number and prints that many numbers starting from 1.
# Input:5 Output: 1 2 3 4 5

def noStart(no):
    ret=0
    for i in range(1,no+1):
        if no > 0:
            print(i)

def main():
    print("Enter one number : ")
    no=int(input())

    noStart(no)
    
if __name__ == "__main__":
    main()