nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]
answer = 987654321


def solution(board):
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]

    def dfs(i, j, direction, cost, visited):
        global answer
        if i == j == len(board)-1:
            answer = min(answer, cost)
            return
        for move in range(4):
            nx = i + nm[move][0]
            ny = j + nm[move][1]
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if direction != move:
                    dfs(nx, ny, move, cost+600, visited)
                else:
                    dfs(nx, ny, move, cost+100, visited)
                visited[nx][ny] = False

    dfs(0, 0, -1, -500, visited)
    return answer


board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
    0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
print(solution(board))
