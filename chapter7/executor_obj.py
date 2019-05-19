from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import threading
import time


def someTask(n):
    print("executing task {}".format(n))
    time.sleep(n)
    print("task {} finished executing".format(n))


def add_task(n):
    print("add task {} {}".format(n, threading.current_thread()))


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(someTask, (1))
        task2 = executor.submit(someTask, (2))
        task3 = executor.submit(someTask, (3))
        task3.add_done_callback(add_task)
        task4 = executor.submit(someTask, (4))


if __name__ == "__main__":
    main()
