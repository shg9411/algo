import itertools
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
for n in list(itertools.combinations(num,m)):
    print(*n)
