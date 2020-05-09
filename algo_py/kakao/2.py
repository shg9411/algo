import re
import itertools


def solution(expression):
    exp = []
    answer = 0
    if '-' in expression:
        exp.append('-')
    if '*' in expression:
        exp.append('*')
    if '+' in expression:
        exp.append('+')
    tmp = list(itertools.permutations(exp, len(exp)))
    tmpexp = re.split('([-*+])', expression)
    for p in tmp:
        res = tmpexp[:]
        tttt = []
        for char in p:
            dummy = False
            for i in range(len(res)):
                if res[i] == char:
                    x = tttt.pop()
                    y = res[i+1]
                    z = eval(x+char+y)
                    tttt.append(str(z))
                    dummy = True
                else:
                    tttt.append(res[i])
                    if dummy:
                        tttt.pop()
                        dummy = False
            res = tttt
        answer = max(answer, abs(int(res[-1])))
    return answer


expression = "50*6-3*2"
print(solution(expression))
