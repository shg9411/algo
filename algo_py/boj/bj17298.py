import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stack = []
res = [-1 for _ in range(N)]
for idx, num in enumerate(A):
    if stack:
        while stack and stack[-1][0] < num:
            _, where = stack.pop()
            res[where] = num
    stack.append([num, idx])
print(*res)