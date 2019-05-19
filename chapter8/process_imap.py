from multiprocessing import Pool
import time


def my_task(n):
    time.sleep(n + 2)
    return n + 2


def main():
    with Pool(4) as p:
        # imap은 풀에 전달된 작업 순서 그대로 출력이 됨.
        for iter in p.imap(my_task, [1, 3, 2, 1]):
            print(iter)


if __name__ == "__main__":
    main()
