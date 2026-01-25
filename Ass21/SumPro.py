# Design a Python application that creates two threads.

# Thread 1 should compute the sum of elements from a list.

# Thread 2 should compute the product of elements from the same list.

# Return the results to the main thread and display them.

import threading
result={}
def Sum(num):
    sum=0
    for data in num:
        sum= sum + data    
        result["sum"]=sum



def Product(num):
    pro=1
    for data in num:
        pro= pro * data
        result["product"]=pro

  

def main():
    print("Enter number of elements: ")
    n = int(input())

    data = []
    print("Enter list elements:")
    for i in range(n):
        value = int(input())
        data.append(value)

    # Create threads
    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads
    t1.join()
    t2.join()

    print("Sum of elements:", result["sum"])
    print("Product of elements:", result["product"])
    print("Exit main thread")


if __name__ == "__main__":
    main()
