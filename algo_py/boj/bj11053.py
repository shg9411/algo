'''
a = int(input())
arr = list(map(int, input().split()))
dp = [0] * a
for i in range(a):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

'''
import bisect


def lis(arr):
    lis_arr = [arr[0]]

    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
    return len(lis_arr)


input()
print(lis(list(map(int, input().split()))))
