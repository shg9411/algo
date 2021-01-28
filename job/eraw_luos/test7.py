import time
import asyncio


var = 0


async def checkAll():
    global cnt
    cnt = 0
    while True:
        await asyncio.sleep(1)
        if var == 3:
            '''
            확인하시려면 주석처리 푸시면 됩니다.
            print("모두 켜짐", time.strftime('%X'))
            '''
            cnt += 1


async def makeBulb(delay):
    global var
    num = -1
    while True:
        await asyncio.sleep(delay)
        num *= -1
        var += num
        print(delay, "on" if num == 1 else "off", time.strftime('%X'))


async def StopWatch(time):
    try:
        await asyncio.wait_for(asyncio.gather(
            makeBulb(3),
            makeBulb(7),
            makeBulb(10),
            checkAll()
        ), timeout=time)
    except asyncio.TimeoutError:
        pass


if __name__ == '__main__':
    print("시작시간", time.strftime('%X'))
    asyncio.run(StopWatch(180.1))
    print("종료시간", time.strftime('%X'))
    print("3개 모두 켜진 시간은 ", cnt)
