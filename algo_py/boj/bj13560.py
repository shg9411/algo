import sys
input = sys.stdin.readline
n = int(input())
score = sorted(list(map(int, input().split())))

s = 0
for i in range(n):
    s += score[i]
    if s < (i+1)*i//2:
        print(-1)
        exit()
print(1 if s == n*(n-1)//2 else -1)
