import sys
import bisect
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]


def lds(i):
    lis_arr = [-arr[i]]

    for n in arr[i+1:]:
        n = -n
        if lis_arr[-1] < n:
            lis_arr.append(n)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
    return len(lis_arr)


def lis(i):
    lis_arr = [arr[i]]

    for n in arr[i+1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
    return len(lis_arr)


res = 0
for i in range(n):
    print(i, lis(i), lds(i))
    res = max(res, lis(i)+lds(i)-1)
print(res)
