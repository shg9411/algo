def solution(n):
    answer = 0
    num_list = [i for i in range(1,n+1)]
    for i in range(0,n//2+2):
        for j in range(i+1,n//2+2):
            if sum(num_list[i:j])==n:
                answer+=1
                break
            if sum(num_list[i:j])>n:
                break
    return answer+1

print(solution(15))