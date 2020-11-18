def solve():
    move = [(1, 1), (1, 0), (1, -1), (0, 1),
            (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    dictionary = dict()

    def dfs(x, y, string, length):
        dictionary[string] = dictionary.get(string, 0)+1
        if length == 5:
            return
        for _x, _y in move:
            tx = (x+_x+n) % n
            ty = (y+_y+m) % m
            dfs(tx, ty, string+tile[tx][ty], length+1)

    n, m, k = map(int, input().split())
    tile = [input() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dfs(i, j, tile[i][j], 1)
    res = []
    for _ in range(k):
        res.append(dictionary.get(input(), 0))
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    solve()