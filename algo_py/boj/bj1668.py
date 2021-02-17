def cnt():
    c = t[0]
    r = 1
    for n in t[1:]:
        if n > c:
            r += 1
            c = n
    return r


t = list(map(int, (input() for _ in range(int(input())))))
print(cnt())
t.reverse()
print(cnt())
