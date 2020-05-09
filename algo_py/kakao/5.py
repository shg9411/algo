def solution(n, path, order):
    arr = [[] for _ in range(n)]
    for i, j in path:
        arr[i].append(j)
        arr[j].append(i)
    answer = True
    return answer


n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
print(solution(n, path, order))
