def solution(n, s):
    if n > s:
        return [-1]
    portion, remainder = divmod(s, n)
    li = [portion] * n
    for i in range(remainder):
        li[i] += 1

    return sorted(li)

n = 2
s = 9
print(solution(n, s))
