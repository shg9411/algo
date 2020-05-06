import sys

n, m = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


def solve(x, y):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            tmp = 'W' if (i+j) % 2 == 0 else 'B'
            if arr[i][j] != tmp:
                count += 1
    return min(64-count, count)

result = []
for i in range(n-7):
    for j in range(m-7):
        result.append(solve(i,j))
print(min(result))
