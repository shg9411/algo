import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for idx, x in enumerate(map(int, input().split())):
        num[i+1][idx+1] = num[i+1][idx] + num[i][idx+1] - num[i][idx] + x

for _ in range(m):
    x, y, i, j = map(int, input().split())
    res = num[i][j] - num[x-1][j] - num[i][y-1] + num[x-1][y-1]
    print(res)
