import sys
input = sys.stdin.readline

n = int(input())
num = list(zip(*[list(map(int, input().split())) for _ in range(n)]))
d = dict()
ans = 0
for n in num[0]:
    for m in num[1]:
        d[n+m] = d.get(n+m, 0)+1

for n in num[2]:
    for m in num[3]:
        ans += d.get(-(n+m), 0)
print(ans)
