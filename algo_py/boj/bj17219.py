import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
    site, pw = input().split()
    d[site] = pw
for _ in range(m):
    print(d[input().rstrip()])
