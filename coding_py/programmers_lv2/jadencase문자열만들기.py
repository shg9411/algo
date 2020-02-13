def solution(s):
    s=list(s.lower())
    tmp = ' '
    for i in range(len(s)):
        if tmp == ' ':
            s[i] = s[i].upper()
        tmp = s[i]
    return ''.join(s)

print(solution('TEST'))