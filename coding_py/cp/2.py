answer = 0
def solution(arr,k,t):
    arr.sort()
    selected = [False for _ in range(len(arr))]
    res = []
    def select(idx):
        global answer
        if sum(res)>t:
            return
        if len(res)>=k:
            answer+=1
        for i in range(idx,len(arr)):
            #if selected[i]:
            #    continue
            selected[i] = True
            res.append(arr[i])
            select(i+1)
            selected[i] = False
            res.pop()
    select(0)
    return answer

arr1 = [1,1,1,1,1]
k1 = 5	
t1 = 10

print(solution(arr1,k1,t1))
