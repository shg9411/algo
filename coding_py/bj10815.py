import sys
input = sys.stdin.readline
n = int(input())
cardSet = set(map(int, input().split()))
m = int(input())
res = []
for n in map(int, input().split()):
    if n in cardSet:
        res.append('1')
    else:
        res.append('0')
print(' '.join(res))
