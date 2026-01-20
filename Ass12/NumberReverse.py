# Write a program which accepts one number and prints that many numbers in reverse order.
# Input:5 Output: 5 4 3 2 1

def noStart(no):
    ret=0
    for i in range(no,0,-1):
        print(i)
       

def main():
    print("Enter one number : ")
    no=int(input())

    noStart(no)
    
if __name__ == "__main__":
    main()