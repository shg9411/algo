import sys
t = int(input())
for _ in range(t):
    r, s = input().split()
    for char in s:
        print(char*int(r), end='')
    print()
