import sys
input = sys.stdin.readline

n,m = map(int,input().split())
x = set()
cnt = 0
for _ in range(n):
    x.add(input().rstrip())
for _ in range(m):
    if input().rstrip() in x:
        cnt+=1
print(cnt)
