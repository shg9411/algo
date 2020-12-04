import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    bottom = list(map(int, input().split()))
    left = list(map(int, input().split()))
    print(len(set(bottom).intersection(set(left))))