def solution(k, score):
    check = dict()
    for idx, grade in enumerate(score[1:], start=1):
        diff = score[idx-1]-grade
        if diff in check:
            check[diff].append(idx+1)
        else:
            check[diff] = [idx+1]
    res = sorted(check.items(), key=lambda x: len(x[1]), reverse=True)
    minus = set()
    for r in res:
        if len(r[1]) < k:
            break
        for cheat in r[1]:
            minus.add(cheat-1)
            minus.add(cheat)
    return len(score)-len(minus) if minus else 0


k = 2
score = [11,10,8,7,6,5]

print(solution(k, score))
