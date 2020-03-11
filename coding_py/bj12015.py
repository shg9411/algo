import bisect


def lis(arr):
    lis_arr = [0]

    for n in arr:
        if lis_arr[-1] < n:
            lis_arr.append(n)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
    return len(lis_arr)-1


input()
print(lis(list(map(int, input().split()))))
