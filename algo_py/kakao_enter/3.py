import sys
input = sys.stdin.readline


def getCount(tmpLen):
    tmpRes = 0
    for c in cookie:
        tmpRes += c//tmpLen
    return tmpRes


N, K = map(int, input().split())
cookie = [int(float(input())*1000) for _ in range(N)]
low = 0
high = max(cookie)
res = 0
while low <= high:
    mid = (low+high)//2
    val = getCount(mid)
    if val < K:
        high = mid-1
    else:
        low = mid+1
        res = mid
print("{:.2f}".format(round(res/1000, 2)))
