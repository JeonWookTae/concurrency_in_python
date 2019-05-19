from multiprocessing import Pool
import os
import time


def my_task(n):
    print("Task process {}".format(os.getpid()))
    time.sleep(n / 2)
    return n * 2


def main():
    with Pool(processes=4) as p:
        # apply는 결과를 갖고 올때까지 작업이 정지되어 있다. 적함 x
        print(p.apply(my_task, (4,)))
        print(p.apply(my_task, (3,)))
        print(p.apply(my_task, (2,)))
        print(p.apply(my_task, (1,)))


def async_main():
    # print(p.apply_async(my_task, (4,))) 결과 값을 리턴해주지 않음
    print("async main")
    with Pool(4) as p:
        tasks = []

        for i in range(10):
            task = p.apply_async(my_task, args=(i,))
            tasks.append(task)
        for task in tasks:
            task.wait()
            print("result {}".format(task.get()))


if __name__ == "__main__":
    async_main()
