import logging
import threading
import time

"""
3.3  Rendezvous

Puzzle: Generalize the signal pattern so that it works both ways. Thread A has to wait for Thread B 
and vice versa. In other words, given this code

Thread A
1 statement  a1
2 statement  a2

Thread B
1 statement  b1
2 statement  b2

we want to guarantee that a1 happens before b2 and b1 happens before a2. 

In writing your solution, be sure to specify the names and initial values of your semaphores (little hint there)

"""

def a(s_a1,s_b1):
    global a1
    logging.info("doing a1")
    a1 = True
    s_a1.release()
    s_b1.acquire()
    assert b1 is True
    logging.info("doing a2")

def b(s_a1,s_b1):
    global b1
    logging.info("doing b1")
    b1 = True
    s_b1.release()
    s_a1.acquire()
    assert a1 is True
    logging.info("doing b2")

a1 = False
b1 = False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    s_a1 = threading.Semaphore(0)
    s_b1 = threading.Semaphore(0)

    a = threading.Thread(target=a, args=(s_a1,s_b1))
    b = threading.Thread(target=b, args=(s_a1,s_b1))

    a.start()
    b.start()

    a.join()
    b.join()

    logging.info("Main end")

