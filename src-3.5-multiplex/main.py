import logging
import threading
import time

"""
3.5  Multiplex

Puzzle: Generalize the previous solution so that it allows multiple threads to run in the critical section at the same time,
but it enforces an upper limit on the number of concurrent threads. 
 
In other words, no more thannthreads canrun in the critical section at the same time. 
 
This pattern is called a multiplex. In real life, the multiplex problem occurs at busy nightclubs where 
there is a maximum number of people allowed in the building at a time, either to maintain fire safety or to 
createthe illusion of exclusivity

"""

import random

def count(mutex):
    global x
    mutex.acquire()
    temp = x
    time.sleep(random.random() / 100)
    x=temp+1
    mutex.release()

x = 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    n = 10
    mutex = threading.Semaphore(n)

    print(x)

    threads = []
    for t in range(100):
        t = threading.Thread(target=count, args=(mutex,)) 
        t.start()
        print(x)
        threads.append(t)

    for thread in threads:
        thread.join()

    print(x)

    logging.info("Main end")

