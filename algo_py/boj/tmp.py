n, m = map(int, input().split())
tree = sorted(map(int, input().split()))
l = 1
r = tree[-1]
res = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for t in tree[::-1]:
        if t > mid:
            cnt += t-mid
        else:
            break
    if cnt >= m:
        l = mid+1
        res = max(res, mid)
    else:
        r = mid-1
print(res)
