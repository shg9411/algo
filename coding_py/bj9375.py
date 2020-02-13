import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        small, mid = input().split()
        if mid in clothes:
            clothes[mid] += 1
        else:
            clothes[mid] = 1
    res = 1
    for var in clothes.values():
        res*=(var+1)
    print(res-1)