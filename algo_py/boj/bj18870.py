import sys
input = sys.stdin.readline
input()
tmp = list(map(int, input().split()))
x = dict()
for idx, num in enumerate(sorted(list(set(tmp)))):
    x[num] = str(idx)
sys.stdout.write(' '.join(x[num] for num in tmp))
