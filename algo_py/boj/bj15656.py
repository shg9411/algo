import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

for res in itertools.product(sorted(map(int, input().split())), repeat=M):
    print(*res)
