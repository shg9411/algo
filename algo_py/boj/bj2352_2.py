import sys
import bisect
input = sys.stdin.readline

n = int(input())
port = list(map(int, input().split()))

lis = [port[0]]

for num in port[1:]:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = bisect.bisect_left(lis, num)
        lis[idx] = num
print(len(lis))
