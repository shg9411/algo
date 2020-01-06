import itertools

n, m = map(int, input().split())
num = list(map(int, input().split()))
res = list(set(itertools.permutations(num,m)))
res.sort()
for r in res:
    print(' '.join(map(str,r)))
