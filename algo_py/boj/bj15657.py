import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

for res in sorted(set(itertools.combinations(sorted(map(int, input().split())), M))):
    print(*res)
