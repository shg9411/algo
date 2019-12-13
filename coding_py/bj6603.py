from itertools import combinations

while 1:
    ks = list(map(int, input().split()))
    if ks[0] == 0:
        break
    k = ks[0]
    s = ks[1:]
    result = list(combinations(s, 6))
    for r in result:
        for rr in r:
            print(rr, end=' ')
        print()
    print()
