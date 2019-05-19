import multiprocessing
from multiprocessing import Pool


def task(n):
    print(n, multiprocessing.current_process().pid)
    return n * 2


def main():
    with Pool(4) as p:
        print(p.map(task, [2, 3, 4, 5]))


if __name__ == "__main__":
    main()
