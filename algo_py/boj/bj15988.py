import sys
input = sys.stdin.readline
cnt = [0, 1, 2, 4]
MOD = 1000000009

for i in range(4, 1000001):
    cnt.append(sum(cnt[-3:]) % MOD)

for _ in range(int(input())):
    print(cnt[int(input())])
