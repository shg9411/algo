import bisect

def lis():
    lis_arr = [-arr[0]]
    for n in arr[1:]:
        n = -n
        if lis_arr[-1] < n:
            lis_arr.append(n)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
    return len(lis_arr)


n = int(input())
arr = list(map(int, input().split()))
print(lis())
