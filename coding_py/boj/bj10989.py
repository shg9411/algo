import sys
n = int(input())
su = [0]*10001
for _ in range(n):
    su[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(su[i]):
        print(i)
