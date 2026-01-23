
# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

# Input :
# Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5

# Output :
# 3

def freqCount(data,search):
    count=0
    for i in data:
        if i == search:
            count+=1
    return count

def main():
    print("Enter the numbers : ")
    no=int(input())

    data=list()
    print("Enter the list elements : ")
    for _ in range(no):
        value=int(input())
        data.append(value)

    print("Enter number to search : ")
    s=int(input())

    result=freqCount(data,s)
    print("Search count is : ",result)
    
if __name__ == "__main__":
    main()
