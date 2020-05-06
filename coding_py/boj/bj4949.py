import sys
check = '([])'
while 1:
    text = sys.stdin.readline()
    if text == ".\n":
        break
    tmp = []
    for char in text:
        if char in check:
            if char == ')' and len(tmp) > 0 and tmp[-1] == '(':
                tmp.pop()
            elif char == ']' and len(tmp) > 0 and tmp[-1] == '[':
                tmp.pop()
            else:
                tmp.append(char)
    print('yes' if not tmp else 'no')
