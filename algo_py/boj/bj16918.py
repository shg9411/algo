def solve():
    r, c, n = map(int, input().split())
    if n == 1:
        for _ in range(r):
            print(input())
    elif not n % 2:
        for _ in range(r):
            print('O'*c)
    else:
        b = [[] for _ in range(r)]
        for i in range(r):
            for v in input():
                b[i].append(1 if v == 'O' else 0)
        n = 2 if n % 4 == 1 else 1
        for _ in range(n):
            t = [[1]*c for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    if b[i][j]:
                        t[i][j] = 0
                        if i + 1 < r:
                            t[i+1][j] = 0
                        if j + 1 < c:
                            t[i][j+1] = 0
                        if i:
                            t[i-1][j] = 0
                        if j:
                            t[i][j-1] = 0
            b = [t[i][:] for i in range(r)]
        for l in t:
            print(''.join(('O' if i else '.' for i in l)))


if __name__ == '__main__':
    solve()