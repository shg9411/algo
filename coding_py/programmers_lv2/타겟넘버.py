res = 0



def solution(numbers, target):
    def dfs(idx,num):
        global res
        if idx == len(numbers):
            if num==target:
                res+=1
            return
        dfs(idx+1,num+numbers[idx])
        dfs(idx+1,num-numbers[idx])
    dfs(0,0)
    return res


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))