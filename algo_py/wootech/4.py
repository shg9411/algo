from collections import deque

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def solution(n, board):
    def delNum(num, i, j):
        visited = [[False]*n for _ in range(n)]
        dq = deque([(i, j)])
        visited[i][j] = True
        cnt = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                if board[x][y] == num:
                    return cnt, x, y
                for _x, _y in move:
                    if not visited[(x+_x) % n][(y+_y) % n]:
                        dq.append(((x+_x) % n, (y+_y) % n))
                        visited[(x+_x) % n][(y+_y) % n] = True
            cnt += 1

    i, j = 0, 0
    answer = n**2
    for num in range(1, n**2+1):
        cnt, i, j = delNum(num, i, j)
        answer += cnt
        # print(num,answer)
    return answer
