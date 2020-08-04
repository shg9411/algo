string = input()+' '
postfix = []
other = []
tmp = ''
oper = {'+': 0, '-': 0, '<?': 1, '>?': 1, '(': -1}
length = len(string)
i = 0
while i < length:
    if '0' <= string[i] <= '9':
        tmp += string[i]
    else:
        if tmp:
            postfix.append(int(tmp))
            tmp = ''
        if string[i] == ' ':
            break
        if string[i] == '(':
            other.append(string[i])
        elif string[i] == ')':
            while other[-1] != '(':
                postfix.append(other.pop())
            other.pop()
        else:
            if string[i] == '<' or string[i] == '>':
                op = string[i]+string[i+1]
                i += 1
            else:
                op = string[i]
            while other and oper[other[-1]] >= oper[op]:
                postfix.append(other.pop())
            other.append(op)
    i += 1

while other:
    postfix.append(other.pop())

stack = []

for x in postfix:
    if isinstance(x, int):
        stack.append(x)
    else:
        second = stack.pop()
        if x == '+':
            stack.append(stack.pop()+second)
        elif x == '-':
            stack.append(stack.pop()-second)
        elif x == '<?':
            stack.append(min(stack.pop(), second))
        else:
            stack.append(max(stack.pop(), second))
print(stack[0])