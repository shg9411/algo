import sys
import bisect
input = sys.stdin.readline

x = int(input())
num = list(map(int, input().split()))

lis_arr = [num[0]]
for n in num[1:]:
    if lis_arr[-1] < n:
        lis_arr.append(n)
    else:
        tmp = bisect.bisect_left(lis_arr, n)
        lis_arr[tmp] = n
print(x-len(lis_arr))
