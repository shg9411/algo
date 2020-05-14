import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
stack = []
res = [-1 for _ in range(N)]
for idx, num in enumerate(A):
    val = cnt[num]
    while stack and stack[-1][0] < val:
        res[stack.pop()[1]] = num
    stack.append([val, idx])
print(*res)