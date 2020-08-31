from collections import deque


def solve():
    n = int(input())
    x = [list(input()) for _ in range(n)]
    res = []

    def bfs(i, j):
        cnt = 1
        x[i][j] = 0
        q = deque()
        q.append((i, j))
        while q:
            i, j = q.popleft()
            if i > 0 and x[i-1][j] == '1':
                x[i-1][j] = 0
                q.append((i-1, j))
                cnt += 1
            if j > 0 and x[i][j-1] == '1':
                x[i][j-1] = 0
                q.append((i, j-1))
                cnt += 1
            if i < n-1 and x[i+1][j] == '1':
                x[i+1][j] = 0
                q.append((i+1, j))
                cnt += 1
            if j < n-1 and x[i][j+1] == '1':
                x[i][j+1] = 0
                q.append((i, j+1))
                cnt += 1
        res.append(cnt)

    for i in range(n):
        for j in range(n):
            if x[i][j] == '1':
                bfs(i, j)
    print(len(res))
    print('\n'.join(map(str,sorted(res))))

if __name__ == '__main__':
    solve()
