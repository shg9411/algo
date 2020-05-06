def partition(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
        if not stack:
            return[s[:i+1], s[i+1:]]


def correct(u):
    stack = []
    for char in u:
        try:
            if char == ')':
                stack.pop()
            else:
                stack.append(char)
        except:
            return False
    return True if not stack else False


def partSolution(w):
    tmp = ''
    if w == '':
        return ''
    [u, v] = partition(w)
    if correct(u):
        tmp = u + partSolution(v)
    else:
        tmp = '('+partSolution(v)+')'
        for char in u[1:-1]:
            if char =='(':
                tmp+=')'
            else:
                tmp+='('
    return tmp


def solution(w):
    if correct(w):
        return w
    answer = partSolution(w)
    return answer

print(solution(')(()'))