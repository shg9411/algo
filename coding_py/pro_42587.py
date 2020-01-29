def solution(priorities, location):
    answer = 0
    end = False
    while not end:
        for i,val in enumerate(priorities):
            mv = max(priorities)
            if val==mv:
                answer+=1
                if i == location:
                    end = True
                    break
                priorities[i] = 0
    return answer


priorities = [2,1,3,2]
location = 2
print(solution(priorities,location))