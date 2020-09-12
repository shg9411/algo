from itertools import combinations


def solution(orders, course):
    orders.sort(key=lambda x: len(x))
    t = dict()
    for order in orders:
        for c in course:
            for com in combinations(order, c):
                com = ''.join(sorted(com))
                if com in t:
                    t[com] += 1
                else:
                    t[com] = 1
    ans = []
    for c in course:
        m = 0
        for k, v in t.items():
            if len(k) == c:
                m = max(v, m)
        if m < 2:
            continue
        for k, v in t.items():
            if len(k) == c and v == m:
                ans.append(k)
    return sorted(ans)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# okay
