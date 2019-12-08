import bisect
import sys
n = int(input())
left_side = list(map(int, sys.stdin.readline().split()))

lis = [left_side[0]]

for i in left_side[1:]:
    if i > lis[-1]:
        lis.append(i)
    else:
        idx = bisect.bisect_left(lis, i)
        lis[idx] = i
print(len(lis))
