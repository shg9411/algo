import sys
input = sys.stdin.readline
for p in sorted([tuple(map(int, input().split())) for _ in range(int(input()))]):
    print(*p)
