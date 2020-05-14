string = list(input().rstrip())
if not string[0] == string[-1] == 'P':
    print('NP')
    exit()
stack = []
length = 0
for char in string:
    stack.append(char)
    if char == 'P':
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(3):
                stack.pop()
print('PPAP' if stack == ['P'] else 'NP')