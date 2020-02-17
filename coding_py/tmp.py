from collections import deque


def bfs():
    while queue:
        print(queue)
        x, y, is_water, cnt = queue.popleft()
        if (x, y) == end:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] != 'X':  # 가려는 곳이 범위에 맞고 돌이 아니면
                if is_water:
                    if matrix[nx][ny] != '*':
                        if matrix[nx][ny] == '.':
                            matrix[nx][ny] = '*'
                            queue.append((nx, ny, True, 0))
                else:
                    if not visited[nx][ny] and matrix[nx][ny] == '.' and matrix[nx][ny] != '*':
                        visited[nx][ny] = True
                        queue.append((nx, ny, False, cnt+1))

    return 'KAKTUS'


r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(c)]  # input값이 space없이 다 붙어있는 string이므로 list()를 이용함
visited = [[False]*r for _ in range(c)]
water_list = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'S':
            start = (i, j, False, 0)  # 0은 고슴도치가 몇칸 갔는지 세려는 용도
        if matrix[i][j] == 'D':
            end = (i, j)
        if matrix[i][j] == '*':
            water_list.append((i, j, True, 0))  # 고슴도치의 좌표와 물의 좌표를 같은 큐에 넣으므로 True, False로 구별해줌

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
for water in water_list:  # 고슴도치가 이동할 차례에 물도 그 자리에 차면 이동을 못하므로 물부터 큐에 넣는다.
    queue.append(water)

queue.append(start)
start_x, start_y, k, m = start  # k랑 m은 필요없음
visited[start_x][start_y] = True
result = bfs()
print(result)
