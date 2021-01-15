import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = list(zip(*[list(map(int, input().split())) for _ in range(n)]))
sa = []
sb = []
ans = 0
for i in range(n):
    for j in range(n):
        sa.append(num[0][i]+num[1][j])
        sb.append(-num[2][i]-num[3][j])

sa = Counter(sa)
sb = Counter(sb)
for k, v in sa.items():
    try:
        ans += v*sb[-k]
    except:
        pass
    #print(sb.get(-k))
print(ans)
