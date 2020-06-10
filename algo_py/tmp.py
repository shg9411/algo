def solution(S):
    cmd = S.split()
    stack = []
    for string in cmd:
        try:
            int(string)
            stack.append(int(string))
        except:
            try:
                if string == "DUP":
                    stack.append(stack[-1])
                elif string == "POP":
                    stack.pop()
                elif string == "+":
                    tmp = stack.pop()+stack.pop()
                    stack.append(tmp)
                elif string == "-":
                    tmp = stack.pop()-stack.pop()
                    stack.append(tmp)
            except:
                return -1
    return stack[-1]


S = "5 6 + -"
solution(S)
