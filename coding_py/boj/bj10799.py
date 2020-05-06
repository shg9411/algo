import sys

line = list(sys.stdin.readline().rstrip())
stick = 0
stack = []
for char in line:
    if char == '(':
        stack.append(char)
    else:
        stack.pop()
        if tmp == '(':
            stick += len(stack)
        else:
            stick += 1
    tmp = char
print(stick)
