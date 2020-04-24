import sys
input = sys.stdin.readline


def dfs(i):
    for want in stone[i]:
        if check[want]:
            continue
        check[want] = True
        if matching[want] == 0 or dfs(matching[want]):
            matching[want] = i
            return True 
    return False 


n, k = map(int, input().split())
stone = [[] for _ in range(n+1)]
matching = [0 for _ in range(n+1)]
res = 0
for _ in range(k):
    i,j = map(int,input().split())
    stone[i].append(j)

for i in range(1, n+1):
    check = [False for _ in range(n+1)] #방문 여부 리스트
    if dfs(i):
        res += 1

print(res)
