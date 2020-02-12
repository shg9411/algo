import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(input().rstrip())
nlen = len(num)

stack = []
i = 0
while k:
    if stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    elif nlen-i <= k:
        i += k
        k = 0
    else:
        stack.append(num[i])
        i += 1


for k in range(i, n):
    stack.append(num[k])

print(''.join(stack))
