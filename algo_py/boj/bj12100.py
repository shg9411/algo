import sys
from collections import deque
sys.setrecursionlimit(10**9)
N = int(input())

res = 0


def getVal():
    global res
    tmp = 0
    for line in board:
        tmp = max(tmp, max(line))
    res = max(res, tmp)


def move(idx):
    q = deque()
    if idx == 0:
        for j in range(N):
            for i in range(N):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j] = 0
            tmp = 0
            while q:
                val = q.popleft()
                if not board[tmp][j]:
                    board[tmp][j] = val
                elif board[tmp][j] == val:
                    board[tmp][j] += val
                    tmp += 1
                else:
                    tmp += 1
                    board[tmp][j] = val
    elif idx == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j] = 0
            tmp = N-1
            while q:
                val = q.popleft()
                if not board[tmp][j]:
                    board[tmp][j] = val
                elif board[tmp][j] == val:
                    board[tmp][j] += val
                    tmp -= 1
                else:
                    tmp -= 1
                    board[tmp][j] = val
    elif idx == 2:
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j] = 0
            tmp = 0
            while q:
                val = q.popleft()
                if not board[i][tmp]:
                    board[i][tmp] = val
                elif board[i][tmp] == val:
                    board[i][tmp] += val
                    tmp += 1
                else:
                    tmp += 1
                    board[i][tmp] = val
    elif idx == 3:
        for i in range(N):
            for j in range(N-1, -1, -1):
                if board[i][j]:
                    q.append(board[i][j])
                    board[i][j] = 0
            tmp = N-1
            while q:
                val = q.popleft()
                if not board[i][tmp]:
                    board[i][tmp] = val
                elif board[i][tmp] == val:
                    board[i][tmp] += val
                    tmp -= 1
                else:
                    tmp -= 1
                    board[i][tmp] = val


def dfs(cnt):
    global board
    if cnt == 5:
        getVal()
        return
    origin = [board[i][:] for i in range(N)]
    for idx in range(4):
        move(idx)
        dfs(cnt+1)
        board = [origin[i][:] for i in range(N)]


def main():
    global board
    board = [list(map(int, input().split())) for _ in range(N)]
    dfs(0)
    print(res)


if __name__ == '__main__':
    main()