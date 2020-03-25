import bisect


def lds():
    lds_arr = [-arr[0]]
    for n in arr[1:]:
        n = -n
        if lds_arr[-1] < n:
            lds_arr.append(n)
        else:
            where = bisect.bisect_left(lds_arr, n)
            lds_arr[where] = n
    return len(lds_arr)


n = int(input())
arr = list(map(int, input().split()))
print(lds())
