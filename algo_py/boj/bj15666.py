import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

for res in sorted(itertools.combinations_with_replacement(sorted(set(map(int, input().split()))), M)):
    print(*res)
