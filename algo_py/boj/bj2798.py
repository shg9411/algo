from itertools import combinations
n, m = map(int, input().split())
res = -1
for c in combinations(map(int, input().split()), 3):
    if (r := sum(c)) <= m:
        res = max(r, res)
print(res)
