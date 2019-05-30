import asyncio


@asyncio.coroutine
def hellow_world():
    yield from asyncio.sleep(1)
    print('hello world')
    asyncio.async(hellow_world())


@asyncio.coroutine
def good_evening():
    yield from asyncio.sleep(1)
    print('good evening')
    asyncio.async(good_evening())
    print("step: asyncio.get_event_loop()")
    loop = asyncio.get_event_loop()
    try:
        print('step: loop.run_untill_complete')
        asyncio.async(hellow_world())
        asyncio.async(good_evening())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('step: loop.close()')
        loop.close()


if __name__ == "__main__":
    good_evening()
