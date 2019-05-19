from concurrent.futures import ThreadPoolExecutor
import threading
import random
import time


def task():
    print("executting our task")
    result = 0
    for i in range(10):
        result += random.randint(1, 5)
        time.sleep(0.01)
    print("I: {} {}".format(result, threading.current_thread()))
    print("task executed {}".format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(fn=task)
    task2 = executor.submit(fn=task)
    task3 = executor.submit(fn=task)
    task4 = executor.submit(fn=task)


if __name__ == "__main__":
    main()

