import sys
input = sys.stdin.readline
string = input().rstrip()
bomb = input().rstrip()
tmp = list(bomb)
bl = len(bomb)
stack = []
for char in string:
    stack.append(char)
    if char == bomb[-1]:
        if stack[-bl:] == tmp:
            for _ in range(bl):
                stack.pop()
print(''.join(stack) if stack else "FRULA")
