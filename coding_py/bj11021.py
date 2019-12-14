import sys
t = int(input())
for i in range(t):
    print("Case #%d:" % (i+1), sum(map(int, sys.stdin.readline().split())))
