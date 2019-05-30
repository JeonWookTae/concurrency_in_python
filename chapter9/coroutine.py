from asyncio import coroutine
import asyncio
import time


@coroutine
def my_test(n):
    time.sleep(1)
    print("Processing: {}".format(n))


@coroutine
def my_generator():
    for i in range(5):
        asyncio.ensure_future(my_test(i))
    print("complete tasks")
    yield from asyncio.sleep(2)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_generator())
    loop.close()


if __name__ == "__main__":
    main()