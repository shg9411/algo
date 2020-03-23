import sys
input = sys.stdin.readline
input()
num = set(map(int, input().split()))
input()
res = []
for n in map(int, input().split()):
    res.append('1') if n in num else res.append('0')
print('\n'.join(res))
