from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    k = limit/2
    while people:
        if people[0]>k:
            answer+=len(people)
            break
        if len(people)>1 and people[0]+people[-1]<=limit:
            answer+=1
            people.popleft()
            people.pop()
        else:
            answer+=1
            people.pop()
    return answer


people = [51,51,51]
limit = 100
print(solution(people, limit))
