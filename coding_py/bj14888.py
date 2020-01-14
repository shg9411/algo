import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
p, m, mp, d = map(int, input().split())

maxV = -1000000001
minV = 1000000001


def calculation(val, idx, p, m, mp, d):
    global minV, maxV
    if idx == n-1:
        if val > maxV:
            maxV = val
        if val < minV:
            minV = val
        return
    idx += 1
    if p > 0:
        val1 = val+num[idx]
        calculation(val1, idx, p-1, m, mp, d)
    if m > 0:
        val2 = val-num[idx]
        calculation(val2, idx, p, m-1, mp, d)
    if mp > 0:
        val3 = val*num[idx]
        calculation(val3, idx, p, m, mp-1, d)
    if d > 0:
        val4 = int(val/num[idx])
        calculation(val4, idx, p, m, mp, d-1)


calculation(num[0], 0, p, m, mp, d)
print(maxV)
print(minV)
