import sys
while True:
    string1 = list(sys.stdin.readline().rstrip())
    if string1[0] == '.':
        break
    string = []
    for letter in string1:
        if '(' == letter or ')' == letter or '[' == letter or ']' == letter or '.' == letter:
            string.append(letter)
    if len(string) == 1:
        print('yes')
        continue
    i = 0
    while len(string) != 1:
        if string[i] == '(' and string[i+1] == ')':
            j = i
            string.pop(i+1)
            string.pop(i)
            if len(string) == 1:
                print('yes')
                break
            elif i != 0:
                i = j-1
                continue
            elif i == 0:
                continue

        elif string[i] == '[' and string[i+1] == ']':
            j = i
            string.pop(i+1)
            string.pop(i)
            if len(string) == 1:
                print('yes')
                break
            elif i != 0:
                i = j-1
                continue
            elif i == 0:
                continue

        elif string[i] == '(' and string[i+1] == ']':
            print('no')
            break
        elif string[i] == '[' and string[i+1] == ')':
            print('no')
            break
        elif string[i] == ')' or string[i] == ']':
            print('no')
            break
        i += 1
