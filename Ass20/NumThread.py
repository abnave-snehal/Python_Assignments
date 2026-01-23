# 5. Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should:
# Display numbers from 1 to 50.

# Thread2 should:
# Display numbers from 50 to 1 in reverse order.

# Ensure that:
# Thread2 starts execution only after Thread1 has completed.

# Use appropriate thread synchronization.
import threading

def countNum(no):
    for i in range(1,no+1):
        print("Thread1",i)

def reverseNum(no):
    for i in range(no,0,-1):
        print("Thread2",i)

def main():

    t1=threading.Thread(target=countNum,args=(50,))
    t2=threading.Thread(target=reverseNum,args=(50,))

    t1.start()

    t1.join()

    t2.start()

    
    t2.join()

if __name__ == "__main__":
    main()