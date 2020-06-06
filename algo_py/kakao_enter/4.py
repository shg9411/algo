import sys
input = sys.stdin.readline


def change(string):
    res = 0
    i = 0
    for char in string[::-1]:
        if char == 'o':
            res += 1 << i
        i += 1
    return res


def floyd(n):
    for k in range(1 << n):
        for i in range(1 << n):
            for j in range(1 << n):
                if info[i][j] > info[i][k] + info[k][j]:
                    info[i][j] = info[i][k] + info[k][j]


N, M = map(int, input().split())
info = [[sys.maxsize for _ in range(1 << N)] for _ in range(1 << N)]
for _ in range(M):
    before, after, cost = input().split()
    before, after = change(before), change(after)
    info[before][after] = min(int(cost), info[before][after])

for i in range(1 << N):
    info[i][i] = 0

floyd(N)

for _ in range(int(input())):
    before, after = input().split()
    before, after = change(before), change(after)
    print(info[before][after] if info[before][after] < sys.maxsize else -1)
