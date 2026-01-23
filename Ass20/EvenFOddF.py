# 2. Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors.

# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
# “Exit from main”
import threading

def EvenFact(no):
    Sumeven=0
    for i in range(1,no+1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            Sumeven+=i
    print("Even sum is :",Sumeven)


def OddFact(no):
    Sumodd=0
    for i in range(1,no+1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            Sumodd+=i
    print("Odd sum is : ",Sumodd)

def main():
    print("Enter the number : ")
    no=int(input())

    t1=threading.Thread(target=EvenFact,args=(no,))
    t2=threading.Thread(target=OddFact,args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main : ")

if __name__ == "__main__":
    main()