def solution(A):
    result = 0
    tmp = sorted(A)
    count = [0 for _ in range(6)]
    li = [0 for _ in range(6)]
    for k in tmp:
        li[k-1]+=1
        li[6-k]-=2
        count[k-1]+=1
    num = li.index(max(li))+1
    for k in tmp:
        if k is not num :
            if k + num == 7:
                result += 1
            result += 1
    return result

print(solution([1,1,4,3,2,6,1]))
