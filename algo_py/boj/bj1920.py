import sys
input = sys.stdin.readline
input()
num = set(input().split())
input()
res = []
for n in input().split():
    res.append(n in num)
print('\n'.join(['1' if r else '0' for r in res]))
