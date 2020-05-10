
def solution(arr):
    tmp = [[] for _ in range(max(arr)+1)]
    for i in arr:
        x = 1
        while i > 2:
            if i % 2 != 0:
                break
            i = i//2
            x += 1
        tmp[i].append(x)
    return tmp


weights = [2,3,4,5,6]
print(solution(weights))
