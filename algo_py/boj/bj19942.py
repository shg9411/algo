n = int(input())
pfsv = list(map(int, input().split()))
base = [list(map(int, input().split())) for _ in range(n)]
candidate = dict()
total = 987654321
for i in range(1, 1 << n):
    tmp = [0]*5
    tres = []
    for j in range(n):
        if (i & (1 << j)):
            tres.append(j+1)
            tmp[0] += base[j][0]
            tmp[1] += base[j][1]
            tmp[2] += base[j][2]
            tmp[3] += base[j][3]
            tmp[4] += base[j][4]
    if tmp[0] >= pfsv[0] and tmp[1] >= pfsv[1] and tmp[2] >= pfsv[2] and tmp[3] >= pfsv[3] and tmp[-1] <= total:
        total = tmp[-1]
        if total in candidate:
            candidate[total].append(tres)
        else:
            candidate[total] = [tres]

if total < 987654321:
    print(total)
    print(*sorted(candidate[total])[0])
else:
    print(-1)
