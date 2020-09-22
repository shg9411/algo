import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i):
    visited[i] = True
    for j in tr[i]:
        if (idx := matching.get(j, -1)) == -1 or (not visited[idx] and dfs(idx)):
            r[i] = j
            matching[j] = i
            return True
    return False


n = int(input())
t = []
tr = []
for i in range(n):
    t.append(tuple(map(int, input().split())))
    a, b, c = t[-1][0]*t[-1][1], t[-1][0]+t[-1][1], t[-1][0]-t[-1][1]
    tmp = set([a, b, c])
    tr.append(tmp)
r = [-sys.maxsize for _ in range(n)]
matching = dict()
for i in range(n):
    visited = [False for _ in range(n)]
    if not dfs(i):
        print("impossible")
        exit()


for j in range(n):
    op = ''
    if t[j][0]+t[j][1] == r[j]:
        op = '+'
    elif t[j][0]*t[j][1] == r[j]:
        op = '*'
    else:
        op = '-'
    print("{} {} {} {} {}".format(
        t[j][0], op, t[j][1], '=', r[j]))
