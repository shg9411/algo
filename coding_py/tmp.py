T = int(input())
ans = []
for j in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    gal = []
    ins, out = [], []
    for i in range(n):
        gal.append(list(map(int, input().split())))
    for cen in gal:
        if (x1 - cen[0]) ** 2 + (y1 - cen[1]) ** 2 < cen[2] ** 2:
            out.append(cen)
        if (x2 - cen[0]) ** 2 + (y2 - cen[1]) ** 2 < cen[2] ** 2:
            ins.append(cen)
    for i in ins:
        for j in out:
            if i == j:
                ins.remove(i)
                out.remove(i)
    ans.append(len(ins)+len(out))
for i in ans:
    print(i)