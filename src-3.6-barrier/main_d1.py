import logging
import threading
import time

"""
3.6  Barrier

Consider again the Rendezvous problem from Section 3.3. A limitation of the solution we presented is that it does not work with more than two threads. 

Puzzle: Generalize the rendezvous solution. Every thread should run the following code:

Barrier code
1 rendezvou
2 critical  point

The synchronization requirement is that no thread executes critical point until after all threads have executed rendezvous. You can assume that 
there arenthreads and that this value is stored in avariable,n, that is accessible from all threads. 

When the first n−1 threads arrive they should block until thenth thread arrives, at which point all the threads may proceed.
_______________________________
1 n = the  number  of  threads
2 count = 0
3 mutex = Semaphore (1)
4 barrier = Semaphore (0) 
_______________________________

count keeps track of how many threads have arrived.
mutex provides exclu-sive access tocountso that threads can increment it safely.
barrieris locked (zero or negative) until all threads arrive; then it shouldbe unlocked (1 or more).

"""

import random

def critical(i):
    print("Critical! A-Z5 button! [%s]" %i)

def count(i, mutex, barrier, n):
    global x
    logging.info(" begin count... [%s]" %i)
    mutex.acquire()
    temp = x
    time.sleep(random.random() / 100)
    x = temp+1
    mutex.release()

    if x ==n:
        barrier.release()

    barrier.acquire()

    critical(i)

    logging.info(" end count... [%s]" % i)

x = 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    n = 5
    barrier = threading.Semaphore(0)
    mutex = threading.Semaphore(1)
    threads = []
    for i in range(10):
        t = threading.Thread(target=count, args=(i, mutex, barrier, n))
        print('x:', x)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print('x:',x)

    logging.info("Main end")

