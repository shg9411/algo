N = int(input())
numList = [[-1,-1]]

for i in range(1, N + 1):
    numList.append([i, int(input())])


def dfs(now, nxt, start, arr):
    arr.append(now)
    if start == nxt:
        global total
        total.extend(arr)
        return

    for a, b in numList:
        if nxt == a and visited[a] == 0:
            visited[nxt] = 1
            dfs(a, b, start, arr)
            visited[nxt] = 0


visited = [0] * (N + 1)
visited[0] = 1
total = []
for i in range(1, N + 1):
    if visited[i] == 0:
        visited[i] = 1
        dfs(numList[i][0], numList[i][1], numList[i][0], [])


print(len(total))
for v in sorted(total):
    print(v)