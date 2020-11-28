def solution(N):
    answer = [1,2]
    for i in range(3, 10):
        num = N
        t = 1
        j = i
        while num:
            mod = num % j
            if mod:
                t *= mod
            num //= j
        if t >= answer[1]:
            answer[0] = i
            answer[1] = t
    return answer


print(solution(1000000))
