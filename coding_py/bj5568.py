import sys
import itertools
input = sys.stdin.readline
n = int(input())
k = int(input())
num = [int(input()) for _ in range(n)]
res = set()
for tmp in set(itertools.permutations(num,k)):
    res.add(''.join(str(x) for x in tmp))

print(len(res))