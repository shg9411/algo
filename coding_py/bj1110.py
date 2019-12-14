import sys


def cycle(i):
    return i % 10*10 + (i//10 + i % 10) % 10


n = int(sys.stdin.readline())
count = 1
tmp = cycle(n)

while 1:
    if tmp == n:
        print(count)
        break

    tmp = cycle(tmp)
    count += 1
