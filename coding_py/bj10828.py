import sys
input = sys.stdin.readline

n = int(input())
stack = []


def isEmpty():
    return False if stack else True


for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if isEmpty():
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if isEmpty() else 0)
    elif cmd[0] == 'top':
        print(-1 if isEmpty() else stack[-1])
