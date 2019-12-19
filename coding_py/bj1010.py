import sys
input = sys.stdin.readline

t = int(input())

while t:
    t -= 1
    n, m = map(int, input().split())
    a = b = 1
    for i in range(n):
        a *= m-i
        b *= n-i
    print(a//b)
