import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    tmp = input().split()
    print(' '.join(word[::-1] for word in tmp))
