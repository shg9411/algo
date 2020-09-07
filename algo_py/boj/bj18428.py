import itertools


def solve():
    def bfs():
        for x, y in t:
            for i in range(x+1, N):
                if cls[i][y] == 'O':
                    break
                if cls[i][y] == 'S':
                    return False
            for j in range(y+1, N):
                if cls[x][j] == 'O':
                    break
                if cls[x][j] == 'S':
                    return False
            for i in range(x-1, -1, -1):
                if cls[i][y] == 'O':
                    break
                if cls[i][y] == 'S':
                    return False
            for j in range(y-1, -1, -1):
                if cls[x][j] == 'O':
                    break
                if cls[x][j] == 'S':
                    return False
        return True

    N = int(input())
    teacher = [set() for i in range(N)]
    cls = [list(input().split()) for _ in range(N)]
    t = []
    for i in range(N):
        for j in range(N):
            if cls[i][j] == 'T':
                t.append((i, j))
                if i > 0 and cls[i-1][j] == 'X':
                    teacher[i-1].add(j)
                if j > 0 and cls[i][j-1] == 'X':
                    teacher[i].add(j-1)
                if i < N-1 and cls[i+1][j] == 'X':
                    teacher[i+1].add(j)
                if j < N-1 and cls[i][j+1] == 'X':
                    teacher[i].add(j+1)

    candi = [(i, j) for i in range(N) for j in teacher[i]]

    for combi in itertools.combinations(candi, 3):
        for x, y in combi:
            cls[x][y] = 'O'
        if bfs():
            print("YES")
            exit()
        for x, y in combi:
            cls[x][y] = 'X'
    print("NO")


if __name__ == '__main__':
    solve()