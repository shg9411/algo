from collections import deque

def solution(priorities, location):
    p_l = deque(sorted(priorities,reverse=True))
    print(p_l)
    answer = 0
    return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
