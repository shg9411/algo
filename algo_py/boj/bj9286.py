import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    num = int(input())
    print("Case %d:" % i)
    for _ in range(num):
        s = int(input())
        if s != 6:
            print(s+1)
