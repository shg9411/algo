import sys
input = sys.stdin.readline


def dfs(i):
    if check[i]:
        return False
    check[i] = True
    for j in adj[i]:
        if cm[j] == -1 or dfs(cm[j]):
            rm[i] = j
            cm[j] = i
            return True
    return False


n, m = map(int, input().split())
chess = [list(input().split()) for _ in range(n)]
row = [[0 for _ in range(m)] for _ in range(n)]
col = [[0 for _ in range(m)] for _ in range(n)]
x = 0
b = False
for i in range(n):
    for j in range(m):
        if chess[i][j] != '2':
            if not b:
                x += 1
                b = True
            row[i][j] = x
        else:
            b = False
    b = False
y = 0
for j in range(m):
    for i in range(n):
        if chess[i][j] != '2':
            if not b:
                y += 1
                b = True
            col[i][j] = y
        else:
            b = False
    b = False
adj = [[] for _ in range(x+1)]
for i in range(n):
    for j in range(m):
        if chess[i][j] == '0':
            adj[row[i][j]].append(col[i][j])
rm = [-1 for _ in range(x+1)]
cm = [-1 for _ in range(y+1)]
res = 0
for i in range(1, x+1):
    if rm[i] != -1:
        continue
    check = [False for _ in range(5002)]
    if dfs(i):
        res += 1
print(res)