import sys
input = sys.stdin.readline
n = int(input())

sqare = [0]
for _ in range(n):
    sqare.append(int(input()))
sqare.append(0)

stack = [0]
res = 0
for i in range(1, len(sqare)):
    while stack and sqare[stack[-1]] > sqare[i]:
        height = stack.pop()
        x = i-1-stack[-1]
        res = max(res, x*sqare[height])
    stack.append(i)
print(res)
