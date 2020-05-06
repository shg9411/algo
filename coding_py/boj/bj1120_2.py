x, y = input().split()
lx = len(x)
ly = len(y)

tmp = ly
for k in range(ly-lx+1):
    count = 0
    for i in range(lx):
        if x[i] != y[i+k]:
            count += 1
    tmp = min(tmp, count)
print(tmp)
