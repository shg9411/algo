import sys
input = sys.stdin.readline

n = int(input())
stack = []
res = []
mn = 0
for _ in range(n):
    num = int(input())
    if mn < num:
        for i in range(mn+1, num+1):
            stack.append(i)
            res.append('+')
        mn = num
        res.append('-')
        stack.pop()
    else:
        if num == stack[-1]:
            res.append('-')
            stack.pop()
        else:
            print("NO")
            exit()
print('\n'.join(res))
