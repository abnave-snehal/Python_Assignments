# Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from a list.

# Thread 2 should calculate and display the minimum element from the same list.

# The list should be accepted from the user.

import threading

def maxNum(num):
    maximum=num[0]      # Assume 1st element is max
    for data in num:
        if data > maximum:
            maximum=data
    print("Maximu number is : ",maximum)



def minNum(num):
    minimum=num[0]
    for data in num:
        if data < minimum:
            minimum=data
    print("Mininum number is :",minimum)

  

def main():
    print("Enter number of elements: ")
    n = int(input())

    data = []
    print("Enter list elements:")
    for i in range(n):
        value = int(input())
        data.append(value)

    # Create threads
    t1 = threading.Thread(target=maxNum, args=(data,))
    t2 = threading.Thread(target=minNum, args=(data,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads
    t1.join()
    t2.join()

    print("Exit main thread")

if __name__ == "__main__":
    main()
