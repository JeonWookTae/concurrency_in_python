import time
import random
from multiprocessing import Process

def calculater_prime_factors(n):
    primfac = list()
    d = 2
    while d*d < n:
        while (n%d) == 0:
            primfac.append(d)
            n //= d
        d +=  1
    if n > 1:
        primfac.append(n)
    return primfac

def execute_proc():
    for i in range(1000):
        rand = random.randint(2000, 10000000)
        print(calculater_prime_factors(rand))

def main():
    print('start number crunching')
    s = time.time()
    procs = list()

    for i in range(12):
        proc = Process(target=execute_proc, args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    e = time.time()

    total_time = e - s
    print("Execution time: {}".format(total_time) )

if __name__ == "__main__":
    main()