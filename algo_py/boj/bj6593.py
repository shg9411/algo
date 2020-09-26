import sys
from collections import deque
input = sys.stdin.readline


def solve():
    while 1:
        L, R, C = map(int, input().split())
        if L == R == C == 0:
            break
        bd = [[] for _ in range(L)]
        v = [[[False for _ in range(C)]
              for _ in range(R)] for _ in range(L)]
        S = [-1, -1, -1]
        for i in range(L):
            for j in range(R):
                bd[i].append(list(input().rstrip()))
                for k in range(C):
                    if bd[i][j][k] == 'S':
                        S = [i, j, k]
                        v[i][j][k] = True
            input()
        q = deque([S])
        cnt = 0
        can = False
        while q:
            cnt += 1
            l = len(q)
            for _ in range(l):
                k, i, j = q.popleft()
                X = i-1
                if 0 <= X:
                    if bd[k][X][j] == 'E':
                        can = True
                        break
                    if bd[k][X][j] == '.' and not v[k][X][j]:
                        v[k][X][j] = True
                        q.append([k, X, j])
                X += 2
                if X < R:
                    if bd[k][X][j] == 'E':
                        can = True
                        break
                    if bd[k][X][j] == '.' and not v[k][X][j]:
                        v[k][X][j] = True
                        q.append([k, X, j])
                Y = j-1
                if 0 <= Y:
                    if bd[k][i][Y] == 'E':
                        can = True
                        break
                    if bd[k][i][Y] == '.' and not v[k][i][Y]:
                        v[k][i][Y] = True
                        q.append([k, i, Y])
                Y += 2
                if Y < C:
                    if bd[k][i][Y] == 'E':
                        can = True
                        break
                    if bd[k][i][Y] == '.' and not v[k][i][Y]:
                        v[k][i][Y] = True
                        q.append([k, i, Y])
                Z = k-1
                if 0 <= Z:
                    if bd[Z][i][j] == 'E':
                        can = True
                        break
                    if bd[Z][i][j] == '.' and not v[Z][i][j]:
                        v[Z][i][j] = True
                        q.append([Z, i, j])
                Z += 2
                if Z < L:
                    if bd[Z][i][j] == 'E':
                        can = True
                        break
                    if bd[Z][i][j] == '.' and not v[Z][i][j]:
                        v[Z][i][j] = True
                        q.append([Z, i, j])
            if can:
                break
        print("Escaped in {} minute(s).".format(cnt) if can else "Trapped!")


if __name__ == '__main__':
    solve()
