S = input().rstrip()
tmp = dict()
for i in range(len(S)):
    x = S[i:]
    tmp[i] = x
for z in sorted(tmp, key=tmp.get):
    print(z)
