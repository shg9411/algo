from itertools import permutations
n, m = map(int, input().split())
for i in list(permutations([i for i in range(1, n+1)], m)):
    print(' '.join(map(str,i)))
