from collections import deque

n = int(input())
area = []
fish = 0
q = deque()
for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] == 9:
            shark = (i, j)
        elif area[i][j] != 0:
            fish += 1
cur = 2
q = deque([shark])
