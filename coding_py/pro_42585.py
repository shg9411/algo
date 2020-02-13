def solution(arrangement):
    answer = 0
    stack = []
    tmp = ''
    for char in list(arrangement):
        if char == ')':
            if tmp == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer+=1
        else:
            stack.append(char)
        tmp = char
    return answer

arrangement = '()(((()())(())()))(())'
print(solution(arrangement))