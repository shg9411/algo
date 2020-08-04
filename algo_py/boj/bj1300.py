n = int(input())
k = int(input())
l = 1
r = k
while l <= r:
    cnt = 0
    m = (l+r)//2
    for i in range(1, n+1):
        cnt += min(m//i, n)
    if cnt < k:
        l = m+1
    else:
        res = m
        r = m-1
print(res)
