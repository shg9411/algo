import bisect
import copy


def lis(arr):
    lis_arr = [arr[0]]
    res = [0]
    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
            res.append(len(lis_arr)-1)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
            res.append(where)

    i = len(lis_arr)
    tmp = [[] for _ in range(i)]
    for idx, x in enumerate(res):
        tmp[x].append([arr[idx], idx])
    for line in tmp:
        line.sort()

    def dfs(idx, jdx, arr):
        if len(arr) == i:
            xx = copy.deepcopy(arr)
            res_arr.append(xx)
            return
        for x in range(jdx, len(tmp[idx])):
            if not arr or (tmp[idx][x][0] > arr[-1][0] and tmp[idx][x][1] > arr[-1][1]):
                arr.append(tmp[idx][x])
                dfs(idx+1, 0, arr)
                arr.pop()
    res_arr = []
    dfs(0, 0, [])
    res_arr.sort()
    if len(res_arr) >= k:
        for x in res_arr[k-1]:
            print(x[0], end=' ')
    else:
        print(-1)


n, k = map(int, input().split())
lis(list(map(int, input().split())))
