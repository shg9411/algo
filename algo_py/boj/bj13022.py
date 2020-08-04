def fin():
    print(0)
    exit()


string = input()

stack = []

cnt = 0
for char in string:
    if char == 'w':
        if stack:
            if stack[-1] != 'w':
                print(0)
                exit()
        if cnt != 0:
            fin()
        stack.append(char)
    elif char == 'o':
        if stack and stack[-1] == 'w':
            stack.pop()
            cnt += 1
        else:
            fin()
    elif char == 'l':
        if stack:
            if stack[-1] != 'l':
                fin()
        stack.append(char)
    elif char == 'f':
        if stack and stack[-1] == 'l':
            stack.pop()
            cnt -= 1
            if cnt < 0:
                fin()
        else:
            fin()
if not stack and cnt == 0:
    print(1)
else:
    print(0)