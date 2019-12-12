import math
n = input()
l = [0] * 9
for i in n:
    if int(i) == 9:
        l[6] += 1
    else:
        l[int(i)] += 1
if l[6] == max(l) and l.count(max(l))==1:
    print(math.ceil(l[6]/2))
else:
    print(max(l))
