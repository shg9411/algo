from collections import Counter


def solution(grade):
    tmp = Counter(grade)
    answer = dict()
    g = 1
    for k, v in sorted(tmp.items(), reverse=True):
        answer[k] = g
        g += v
    res = [answer[g] for g in grade]
    return res


grade = [3, 2, 1, 2]

print(solution(grade))
