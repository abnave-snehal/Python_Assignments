# Design a Python application that creates two threads named EvenList and OddList.

# Both threads should accept a list of integers as input.

# The EvenList thread should:

# Extract all even elements from the list.

# Calculate and display their sum.

# The OddList thread should:

# Extract all odd elements from the list.

# Calculate and display their sum.

# Threads should run concurrently.
import threading

def EvenList(data):
    Sumeven=0
    print("Even numbers : ")
    for i in data:
        if i % 2 == 0:
            print(i)
            Sumeven+=i
    print("Even sum is :",Sumeven)


def OddList(data):
    Sumodd=0
    print("Odd numbers : ")
    for i in data:
        if i % 2 != 0:
            print(i)
            Sumodd+=i
    print("Odd sum is : ",Sumodd)

def main():
    print("Enter the number : ")
    no=int(input())

    data=list()
    print("Enter the list elemnts : ")
    for i in range(no):
        value=int(input())
        data.append(value)

    t1=threading.Thread(target=EvenList,args=(data,))
    t2=threading.Thread(target=OddList,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main : ")

if __name__ == "__main__":
    main()