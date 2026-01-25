# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should:
# Count and display the number of lowercase characters.

# The Capital thread should:
# Count and display the number of uppercase characters.

# The Digits thread should:
# Count and display the number of numeric digits.

# Each thread must also display:
# Thread ID
# Thread Name

import threading

def small(s):
    count=sum(1 for ch in s if ch.islower())
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())
    print("Lower letters count : ",count)

def cap(s):
    count=sum(1 for ch in s if ch.isupper())
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID :",threading.get_ident())
    print("Upper letter count is :",count)

def digit(s):
    count=sum(1 for ch in s if ch.isdigit())
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())
    print("Digit count is : ",count)



def main():
    print("Enter the string : ")
    strCh=input()

    t1=threading.Thread(target=small,args=(strCh,))
    t2=threading.Thread(target=cap,args=(strCh,))
    t3=threading.Thread(target=digit,args=(strCh,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")
if __name__ == "__main__":
    main()