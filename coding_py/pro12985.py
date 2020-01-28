def solution(n, a, b):
    answer = 0
    while 1:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
        if a == b:
            break
    return answer


print(solution(8, 4, 7))
