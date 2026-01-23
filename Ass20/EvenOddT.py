# Design a Python application that creates two separate threads named Even and Odd.

# The Even thread should display the first 10 even numbers.

# The Odd thread should display the first 10 odd numbers.

# Both threads should execute independently using the threading module.

# Ensure proper thread creation and execution.
import threading

def even():
    print("Even numbers : ")
    for i in range(2,21):
        if i % 2 == 0:
            print(i)

def odd():
    print("Odd number : ")
    for i in range(1,21):
        if i % 2 != 0:
            print(i)

    
def main():
    print("Inside main: ")
    t1=threading.Thread(target=even)
    t2=threading.Thread(target=odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main function : ")

if __name__ == "__main__":
    main()