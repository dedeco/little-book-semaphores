

import logging
import threading
import time


def thread_function(name, seconds):
    logging.info("Thread starting %s", name)
    time.sleep(seconds)
    logging.info("Thread finishing %s", name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    x = threading.Thread(target=thread_function, args=(1,2))
    y = threading.Thread(target=thread_function, args=(2,1))
    logging.info("Main: before running thread")
    x.start()
    y.start()
    logging.info("Main: wait for the thread to finish")
    #x.join()
    y.join()
    logging.info("Main: all done")
    




