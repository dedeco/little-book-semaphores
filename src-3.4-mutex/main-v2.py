import logging
import threading
import time

"""
3.4  Mutex

A second common use for semaphores is to enforce mutual exclusion. 

We have al-ready seen one use for mutual exclusion, controlling concurrent access to sharedvariables. 

The mutex guarantees that only one thread accesses the shared variable at a time. A mutex is like a 
token that passes from one thread to another,allowing one thread at a time to proceed. 

For example, in The Lord of the Flies a group ofc hildren use a conch as a mutex. 

In order to speak, you have to hold the conch.

"""
import random

def count(mutex):
    global x
    mutex.acquire()
    temp = x
    x=temp+1
    mutex.release()

def count2():
    global x
    temp = x
    time.sleep(random.random() / 100)
    x=temp+1

def count3(mutex2):
    global y
    mutex2.acquire()
    temp = y
    time.sleep(random.random() / 100)
    y=temp+1
    mutex2.release()

x = 0
y = 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    mutex = threading.Semaphore(1)

    print(x)

    threads = []
    for t in range(100):
        t = threading.Thread(target=count2) 
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(x)

    mutex2 = threading.Semaphore(1)
    threads = [threading.Thread(target=count3, args=(mutex2,)) for t in range(100)]
    
    print(y)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(y)

    logging.info("Main end")

