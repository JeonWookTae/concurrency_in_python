import multiprocessing
import time


def daemon_process():
    print("start my daemon process")
    print("daemon prcess started: {}".format(multiprocessing.current_process().pid))
    time.sleep(3)
    print("daemon process terminating")
    print("main process: {}".format(multiprocessing.current_process().pid))


def main():
    my_process = multiprocessing.Process(target=daemon_process)
    my_process.daemon = True
    my_process.start()
    print("we can carry on as per usual and our daemon wil continue to execute")
    time.sleep(4)


if __name__ == "__main__":
    main()
