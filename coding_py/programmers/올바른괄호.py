def solution(s):
    stack = []
    if s[0]==')':
        return False
    stack.append('(')
    for i in range(1,len(s)):
        if s[i]==')':
            try:
                stack.pop()
            except:
                return False
        else:
            stack.append('(')
    return True if not stack else False