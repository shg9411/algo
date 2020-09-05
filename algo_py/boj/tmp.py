import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    s = set()
    s.add(x)
    s.add(y)
    n -= 2
    if n == 0:
        print(*s)
        continue
    i = abs(x-y)//n
    print(i)
