def solution(s, op):
    answer = []
    l = len(s)
    for i in range(1,l):
        if op=="+":
            answer.append(sum(map(int,(s[:i],s[i:]))))
        elif op=="-":
            answer.append(int(s[:i])-int(s[i:]))
        else:
            answer.append(int(s[:i])*int(s[i:]))
    return answer