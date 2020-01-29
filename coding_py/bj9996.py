import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip().split('*')

for _ in range(n):
    tmp = input().rstrip()
    if tmp.startswith(pattern[0]) and tmp.endswith(pattern[1]):
        if len(tmp) < len(pattern[0])+len(pattern[1])-1:
            print('NE')
        else:
            print('DA')
    else:
        print('NE')
