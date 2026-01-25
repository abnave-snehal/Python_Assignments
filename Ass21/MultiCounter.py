# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading

cnt=0

lock=threading.Lock()

Increment=10000

def increment_counter():
    global cnt
    for i in range(Increment):
        with lock:
            cnt+=1

threads=[]
num_thread=5

for i in range(num_thread):
    thread=threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final value of a counter : ",cnt)
