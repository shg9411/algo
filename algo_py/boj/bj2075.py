import sys
input = sys.stdin.readline
n, q = int(input()), []
for _ in range(n):
    q = sorted(q+list(map(int, input().split())))[-n:]
print(q[0])
