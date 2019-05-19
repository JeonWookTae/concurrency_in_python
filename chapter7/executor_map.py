from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import threading
import time


values = [2, 3, 4, 5, 6, 7, 8, 9, 0]


def multiply_by_two(n):
    return (2 * n, threading.current_thread())


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiply_by_two, values)
    for result in results:
        print(result)


def someTask(n):
    print("executing task {}".format(n))
    time.sleep(n)
    print("task {} finished executing".format(n))


def main_shutdown():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(someTask, (1))
        task2 = executor.submit(someTask, (2))

        executor.shutdown(wait=True)
        task3 = executor.submit(someTask, (3))
        task4 = executor.submit(someTask, (4))



if __name__ == "__main__":
    main()
    main_shutdown()
