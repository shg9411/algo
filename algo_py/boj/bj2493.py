n = int(input())
high = list(map(int,input().split()))
res = [0 for _ in range(n)]
tmp = []
for idx,val in enumerate(high):
    while tmp:
        if high[tmp[-1]] > val:
            res[idx] = tmp[-1]+1
            break
        tmp.pop()
    if not tmp:
        res[idx] = 0
    tmp.append(idx)
print(' '.join(map(str,res)))