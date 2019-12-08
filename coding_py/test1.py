count = 0
def solution(A,B,C,D):
    li = [A,B,C,D]
    li.sort()
    used = [0 for _ in range(4)]
    def make(k, used):
        global count
        if len(k)>=1 and k[0]>2:
            return
        if len(k)>=2 and k[0]>1 and k[1]>3:
            return
        if len(k)>=3 and k[2]>=6:
            return
        if len(k) == 4:
            count+=1
            return
        for i in range(4):
            if not used[i] and (i==0 or li[i-1] != li[i] or used[i-1]):
                k.append(li[i])
                used[i] = 1
                make(k,used)
                used[i] = 0
                k.pop()
    make([],used)
    return count


print(solution(6,1,4,7))