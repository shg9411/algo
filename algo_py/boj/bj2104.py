def div(i, j):
    if i == j:
        return arr[i]*arr[j]
    m = (i+j)//2
    res = max(div(i, m), div(m+1, j))
    l = m
    r = m+1
    ts = arr[l]+arr[r]
    tv = min(arr[l], arr[r])
    res = max(res, ts*tv)
    while l > i or r < j:
        if r < j and (l == i or arr[l-1] < arr[r+1]):
            r += 1
            ts += arr[r]
            tv = min(tv, arr[r])
        else:
            l -= 1
            ts += arr[l]
            tv = min(tv, arr[l])
        res = max(res, tv*ts)
    return res


n = int(input())
arr = list(map(int, input().split()))
print(div(0, n-1))
