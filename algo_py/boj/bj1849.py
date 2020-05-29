import sys
import math
input = sys.stdin.readline

n = int(input())
res = [0 for _ in range(n)]
tmp = [0 for _ in range(2**(math.ceil(math.log2(n))+1))]


def kth(height, s, e, val):
    tmp[height] += 1
    if s == e:
        return s
    mid = (s+e)//2
    if val <= mid-s+1-tmp[height*2+1]:
        return kth(height*2+1, s, mid, val)
    return kth(height*2+2, mid+1, e, val+tmp[height*2+1]-mid+s-1)


for i in range(1, n+1):
    val = int(input())
    res[kth(0, 0, n-1, val+1)] = i

print(*res, sep='\n')