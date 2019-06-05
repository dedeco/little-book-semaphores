import logging
import threading
import time
import random
import concurrent.futures


def counter(i, mutex):
    global x
    logging.info("Thread %s: starting update", i)
    mutex.acquire()
    temp = x
    time.sleep(random.random() / 100)
    x = temp+1
    mutex.release()
    logging.info("Thread %s: finishing update", i)

x = 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    mutex = threading.Semaphore(1)

    logging.info("Testing update. Starting value is %d.", x)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            executor.submit(counter, i, mutex)
    logging.info("Testing update. Ending value is %d.", x)
