import threading
import time
from numpy import random


class Philosopher(threading.Thread):
    def __init__(self, leftFork, rightFork):
        print("철학자의 저녁식사")
        threading.Thread.__init__(self)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print("philosopher: {} has started thinking".format(threading.current_thread()))
        while True:
            time.sleep(random.randint(1, 5))
            print("philosopher: {} has finished thinking".format(threading.current_thread()))
            self.leftFork.acquire()
            time.sleep(random.randint(1, 5))
            try:
                print("philosopher {} has acquired the left fork".format(threading.current_thread()))
                self.leftFork.acquire()
                try:
                    print("philosopher {} has attained both forks".format(threading.current_thread()))
                finally:
                    self.rightFork.release()
                    print("philosopher {} has released thre right fork".format(threading.current_thread()))
            finally:
                self.leftFork.release()
                print("philosopher {} has released the left fork".format(threading.current_thread()))

                
if __name__ == "__mian__":
    acquire()
