import logging
import threading
import time

"""
3.1 Signaling

Possibly the simplest use for a semaphore is signaling, which means that one thread sends a signal 
to another thread to indicate that something has happened.

"""

def read(x):
    global line
    logging.info("Thread starting reading")
    logging.info("reads a line from a file")
    line = 'Sabe de nada, inocente!'
    logging.info("Thread finishing reading")
    time.sleep(2)
    x.release()

def display(x):
    logging.info("Thread starting display")
    x.acquire()
    assert line is not None
    logging.info("displays the line on the screen")
    print(line)
    logging.info("Thread finishing display")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Main start")

    x = threading.Semaphore(0)

    a = threading.Thread(target=read, args=(x,))
    b = threading.Thread(target=display, args=(x,))

    a.start()
    b.start()

    a.join()
    #b.join()

    logging.info("Main end")

