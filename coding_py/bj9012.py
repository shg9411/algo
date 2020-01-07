import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    tmp = list(input().rstrip())
    check = True
    for char in tmp:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack.pop() == '(':
                continue
            else:
                print('NO')
                check = False
                break
    if check:
        print('YES' if not stack else 'NO')
