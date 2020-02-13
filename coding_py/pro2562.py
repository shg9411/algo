

def solution(n, computers):
    edge = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1 and not edge[j][i]:
                edge[i][j] = True
                edge[j][i] = True
    count = 0
    total = set()
    for i in range(n):
        if i not in total:
            count+=1
            tmp = []
            total.add(i)
            tmp.append(i)
            while tmp:
                com = tmp.pop(0)
                for j in range(n):
                    if edge[com][j] == True and j not in total:
                        total.add(j)
                        tmp.append(j)

    return count


computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, computers))
