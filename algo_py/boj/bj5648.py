import sys
num = []
while l := sys.stdin.readline():
    num.extend(map(lambda x: int(x[::-1]), l.split()))
[*map(print,sorted(num[1:]))]
