import sys
sys.setrecursionlimit(10**9)
s = sys.stdin.readline().split()
N = int(s[0])
M = int(s[1])

max1 = 0


def go(i, j, total, count, code):
    global matrix
    global max1
    total = total + matrix[i][j]
    count = count + 1
    if count == 4:
        if total > max1:
            max1 = total
        return

    if i > 0 and code != 2:
        go(i - 1, j, total, count, 1)
    if i < N - 1 and code != 1:
        go(i + 1, j, total, count, 2)
    if j > 0 and code != 4:
        go(i, j - 1, total, count, 3)
    if j < N - 1 and code != 3:
        go(i, j + 1, total, count, 4)
    return


matrix = []
for i in range(N):
    s = sys.stdin.readline().split()
    matrix.append([int(c) for c in s])

four_max = 0
for i in range(N):
    for j in range(M):
        go(i, j, 0, 0, 0)


for i in range(N):
    for j in range(M-2):
        three = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
        if i >= 1:
            temp = three + matrix[i-1][j+1]
            if temp > max1:
                max1 = temp
        if i < N-1:
            temp = three + matrix[i+1][j+1]
            if temp > max1:
                max1 = temp

for i in range(N-2):
    for j in range(M):
        three = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j]
        if j >= 1:
            temp = three + matrix[i+1][j-1]
            if temp > max1:
                max1 = temp
        if j < M-1:
            temp = three + matrix[i+1][j+1]
            if temp > max1:
                max1 = temp
print(max1)
