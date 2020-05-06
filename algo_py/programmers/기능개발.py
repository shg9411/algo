import math

def solution(progresses, speeds):
    day = 0
    answer = []
    for p,s in zip(progresses,speeds):
        p+=s*day
        if p<100:
            day += math.ceil((100-p)/s)
            answer.append(1)
        else:
            answer[-1]+=1
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses,speeds))