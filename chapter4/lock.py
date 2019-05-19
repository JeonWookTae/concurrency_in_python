import threading
import time
import random

counter = 1
lock = threading.Lock() # 락을 추가


def worker_a():
    global counter
    lock.acquire()
    try:
        while counter < 100:
            counter += 1
            print('workerA counter up {}'.format(counter))
            time.sleep(random.randint(0, 1))
    finally:
        lock.release()


def worker_b():
    global counter
    lock.acquire()
    try:
        while counter > -100:
            counter -= 1
            print('workerB counter up {}'.format(counter))
            time.sleep(random.randint(0, 5))
    finally:
        lock.release()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=worker_a)
    thread2 = threading.Thread(target=worker_b)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print("Execution Time {}".format(t1 - t0))

if __name__ == "__main__":
    main()