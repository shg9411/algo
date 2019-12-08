n = list(map(int, input()))
result = []
if 0 not in set(n):
    print(-1)
else:
    n.remove(0)
    if sum(n) % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        for x in n:
            result.append(x)
        result.append(0)
        print(''.join(map(str,result)))
