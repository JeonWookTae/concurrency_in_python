import threading
import time


def ourThread(i):
    print("thread {} started".format(i))
    time.sleep(i*2)
    print("thread {} finished".format(i))


def main():
    thread1 = threading.Thread(target=ourThread, args=(1,))
    thread1.start()
    print("is thread 1 finished?")
    thread2 = threading.Thread(target=ourThread, args=(2,))
    thread2.start()
    thread2.join()
    print("thread 2 definitely finished")


if __name__ == "__main__":
    main()
