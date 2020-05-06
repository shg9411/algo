s = input()
static = False
tmp = []
answer = ''
for char in s:
    if char=='<':
        if tmp:
            answer+=''.join(tmp[::-1])
            tmp = []
        static = True
        answer+=char
        continue
    if static:
        answer+=char
        if char[-1]=='>':
            static = False
    elif char==' ':
        answer+=''.join(tmp[::-1])+' '
        tmp = []
    else:
        tmp.append(char)
if tmp:
    answer+=''.join(tmp[::-1])

print(answer)



