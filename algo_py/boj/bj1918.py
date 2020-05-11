tmp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
res = ''
line = input().rstrip()
stack = []
for char in line:
    if char == '(':
        stack.append(char)
    elif 'A' <= char <= 'Z':
        res += char
    elif char == ')':
        while stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    else:
        while stack and tmp[stack[-1]] >= tmp[char]:
            res += stack.pop()
        stack.append(char)
while stack:
    res += stack.pop()
print(res)
