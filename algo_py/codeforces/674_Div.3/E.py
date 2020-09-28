import sys
input = sys.stdin.readline

x = int(input())
# 묵 찌 빠
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MAX = min(a[0], b[1])+min(a[1], b[2])+min(a[2], b[0])
MIN = 0
tmp = min(a[0], b[0]+b[2])
a[0] -= tmp
ttmp = min(a[1], b[0]+b[1])
a[1] -= ttmp
tttmp = min(a[2], b[1]+b[2])
a[2] -= tttmp
print(sum(a), MAX)
