n, k = map(int, input().split())

f_t = [0]*100001


def sum(i):
    res = 0
    while i > 0:
        res += f_t[i]
        i -= (i & -i)
    return res


def update(i, diff):
    while i <= n:
        f_t[i] += diff
        i += (i & -i)


def cnt(i, j):
    j = j%n
    if not j:
        j = n
    if j >= i:
        return sum(j)-sum(i)
    return sum(n)-sum(i)+sum(j)


for i in range(1, n+1):
    update(i, 1)
r = [k]
update(k, -1)
c = k
l = n-1
while l > 0:
    s = c+1
    e = c+n
    while s < e:
        m = (s+e) >> 1
        v = cnt(c, m)
        mod = k%l
        if not mod:
            mod = l
        if v < mod:
            s = m+1
        elif v == mod:
            e = m
        else:
            e = m-1
    s = s % n
    if s == 0:
        s = n
    r.append(s)
    c = s
    update(s, -1)
    l -= 1

print('<',', '.join(map(str,r)),'>',sep='')
