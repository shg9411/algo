import sys
input = sys.stdin.readline

while 1:
    sqare = list(map(int, input().split()))
    if sqare[0] == 0:
        break
    sqare[0] = 0
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
