import math


def solution(progresses, speeds):
    answer = []
    before = 0
    for i, j in zip(progresses, speeds):
        day = math.ceil((100-i)/j)
        if day <= before:
            answer[-1]+=1
        else:
            before = day
            answer.append(1)
    return answer


progresses = [5, 5, 5]
speeds = [21, 25, 20]
print(solution(progresses, speeds))
