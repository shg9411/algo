import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))

i = j = 0
minlen = sys.maxsize
tmp = 0

while 1:
    if tmp >= s:
        minlen = min(j-i, minlen)
        tmp -= num[i]
        i += 1
    elif j == n:
        break
    else:
        tmp += num[j]
        j += 1
print(minlen if minlen < sys.maxsize else 0)
