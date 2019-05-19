import multiprocessing
import time


def daemon_process():
    print("child process started: {}".format(multiprocessing.current_process().pid))
    time.sleep(3)
    print("child process terminating")


def main():
    print("main process started: {}".format(multiprocessing.current_process().pid))
    my_process = multiprocessing.Process(target=daemon_process)
    my_process.start()
    my_process.join()


if __name__ == "__main__":
    main()
