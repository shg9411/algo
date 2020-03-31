import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(zip(list(map(int, input().split())), [i for i in range(n)]))
for _ in range(m):
    i, j, k = map(int, input().split())
    idx = 0
    tmp = -10**9-1
    for n in num:
        if i-1 <= n[1] <= j-1:
            if n[0] > tmp:
                tmp = n[0]
                idx += 1
                if idx == k:
                    print(n[0])
                    break
