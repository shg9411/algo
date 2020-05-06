import sys
K = int(input())
signs = list(input().split())
initial = list(range(10))
visited = [0 for _ in range(11)]
min_res = []
max_res = []

def dfs(last, visited, count):
    global found
    if count == K+1 and not found:
        # print(visited)
        res_list = [0 for _ in range(K+1)]
        for i in range(11):
            if visited[i]:
                res_list[visited[i]-1] = i
        found = True
        print(*res_list, sep="")
        return

    if not found:
        sign = signs[count-1]
        if sign == "<":
            for num in range(last+1, 10):
                if not visited[num]:
                    visited[num] = count + 1
                    dfs(num, visited, count + 1)
                    visited[num] = 0

        else:
            for num in range(0, last):
                if not visited[num]:
                    visited[num] = count + 1
                    dfs(num, visited, count + 1)
                    visited[num] = 0

def reverse_dfs(last, visited, count):
    global found
    if count == K+1 and not found:
        res_list = [0 for _ in range(K+1)]
        for i in range(11):
            if visited[i]:
                res_list[visited[i]-1] = i
        found = True
        print(*res_list, sep="")
        return

    if not found:
        sign = signs[count-1]
        if sign == "<":
            for num in range(9, last, -1):
                if not visited[num]:
                    visited[num] = count + 1
                    reverse_dfs(num, visited, count + 1)
                    visited[num] = 0

        else:
            for num in range(last-1, -1, -1):
                if not visited[num]:
                    visited[num] = count + 1
                    reverse_dfs(num, visited, count + 1)
                    visited[num] = 0


found = False
for i in range(9,-1,-1):
    visited[i] = 1
    reverse_dfs(i, visited, 1)
    visited[i] = 0

found = False
for i in range(10):
    visited[i] = 1
    dfs(i, visited, 1)
    visited[i] = 0