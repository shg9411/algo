import sys
input = sys.stdin.readline

n = int(input())

shark = [list(map(int, input().split())) for _ in range(n)]
can_eat = [[] for _ in range(n)]
eaten = [-1 for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            can_eat[i].append(j)
        elif shark[i][0] <= shark[j][0] and shark[i][1] <= shark[j][1] and shark[i][2] <= shark[j][2]:
            can_eat[j].append(i)
# print(can_eat)


def dfs(i):
    for want in can_eat[i]:
        if checked[want]:
            continue
        checked[want] = True
        if eaten[want] == -1 or dfs(eaten[want]):
            eaten[want] = i
            return True
    return False


res = 0
for i in range(n):
    checked = [False for _ in range(n)]
    if dfs(i):
        res += 1
        checked = [False for _ in range(n)]
        if dfs(i):
            res += 1

print(n-res)
