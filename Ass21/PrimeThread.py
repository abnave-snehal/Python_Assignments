# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime(data):
    print("Prime numbers:")
    for num in data:
        if is_prime(num):
            print(num)

def nonPrime(data):
    print("Non-prime numbers:")
    for num in data:
        if not is_prime(num):
            print(num)

def main():
    print("Enter number of elements: ")
    n = int(input())

    data = []
    print("Enter list elements:")
    for i in range(n):
        value = int(input())
        data.append(value)

    # Create threads
    t1 = threading.Thread(target=prime, args=(data,))
    t2 = threading.Thread(target=nonPrime, args=(data,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads
    t1.join()
    t2.join()

    print("Exit main thread")

if __name__ == "__main__":
    main()
