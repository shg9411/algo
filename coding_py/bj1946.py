import sys

def _1946():
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = []
        for j in range(N):
            a, b = map(int, sys.stdin.readline().split())
            arr.append((a, b))

        arr.sort()
        cnt = 0
        aMax = 100001
        bMax = 100001
        for i in arr:
            if i[0] < aMax and i[1] > bMax:
                cnt += 1
                aMax = i[0]
            elif i[0] > aMax and i[1] < bMax:
                cnt += 1
                bMax = i[1]
            elif i[0] < aMax and i[1] < bMax:
                cnt += 1
                aMax = i[0]
                bMax = i[1]
        print(cnt)

_1946()