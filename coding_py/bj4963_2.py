dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

answer = []

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    cnt = 0
    matrix = []
    for _ in range(y):
        matrix.append(list(map(int, input().split())))

    for i in range(y):
        for j in range(x):
            queue = []
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                cnt += 1
                queue.append([i, j])
                while queue:
                    m, n = queue.pop(0)
                    for k in range(8):
                        ax = m+dx[k]
                        ay = n+dy[k]
                        if ax >= 0 and ax < y and ay >= 0 and ay < x:
                            if matrix[ax][ay] == 1:
                                matrix[ax][ay] = 0
                                queue.append([ax, ay])

    answer.append(cnt)

for i in answer:
    print(i)
