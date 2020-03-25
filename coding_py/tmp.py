import bisect

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    lis, lds = [arr[i]], [arr[i]]
    for j in range(i+1, N):
        if lis[-1] < arr[j]:
            lis.append(arr[j])
        else:
            tmp = bisect.bisect_left(lis, arr[j])
            if tmp == 0 and arr[j] < lis[0]:
                continue
            lis[tmp] = arr[j]
    for j in range(i+1, N):
        if lds[-1] > arr[j]:
            lds.append(arr[j])
        else:
            tmp = bisect.bisect_right(lds, arr[j])
            if tmp == 0 and arr[j] > lds[0]:
                continue
            lds[tmp] = arr[j]
    ans = max(ans, len(lis) + len(lds) - 1)
print(ans)
