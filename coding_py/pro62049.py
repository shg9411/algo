def solution(n):
    answer = []
    for _ in range(n):
        answer.append(0)
        for num in answer[-2::-1]:
            if num==0:
                answer.append(1)
            else:
                answer.append(0)
    return answer


for i in range(1, 4):
    print(i, solution(i))
