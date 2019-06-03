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
    time.sleep(random.random() / 10)
    x=temp+1
    mutex.release()

def count2(mutex):
    global x
    temp = x
    time.sleep(random.random() / 10)
    x=temp+1
    
x = 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    mutex = threading.Semaphore(1)

    a = threading.Thread(target=count, args=(mutex,))
    b = threading.Thread(target=count, args=(mutex,))

    print(x)

    a.start()
    b.start()

    a.join()
    b.join()

    print(x)

    logging.info("Main end")

