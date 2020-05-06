import sys
from itertools import combinations
vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, sys.stdin.readline().split())
pwd = sorted(list(map(str, sys.stdin.readline().split())))

combi = combinations(pwd, l)

for com in combi:
    count = 0
    for letter in com:
        if letter in vowels:
            count += 1
    if count >= 1 and count <= l-2:
        print(''.join(com))
