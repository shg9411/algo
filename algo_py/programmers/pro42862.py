def solution(n, lost, reserve):
    answer = [1 for _ in range(n+2)]
    answer[0] = 0
    answer[-1] = 0
    for i in lost:
        answer[i] -= 1
    for i in reserve:
        answer[i] += 1
    for i in range(1, n+1):
        if answer[i] == 0:
            if answer[i-1] > 1:
                answer[i-1] -= 1
                answer[i] = 1
            elif answer[i+1] > 1:
                answer[i+1] -= 1
                answer[i] = 1
    res = 0
    for i in answer:
        if i>=1:
            res+=1
    return res


n = 6
lost = [1,3,5]
reserve = [2,4,6]
print(solution(n, lost, reserve))
