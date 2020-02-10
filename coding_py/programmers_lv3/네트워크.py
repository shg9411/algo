def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if j!=i and computers[i][j]==1 and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1


    return answer


print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))