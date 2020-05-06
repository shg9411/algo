import sys
import bisect
input = sys.stdin.readline
n = int(250000)
bst = []
height = [0 for _ in range(n)]

res = 0

for i in range(n):
    tmp = i
    idx = bisect.bisect_left(bst, tmp)
    first = height[bst[idx-1]] if idx > 0 else 0
    second = height[bst[idx]] if idx < len(bst) else 0
    height[tmp] = max(first, second)+1
    bst.insert(idx, tmp)
    res += height[tmp]
print(res)
