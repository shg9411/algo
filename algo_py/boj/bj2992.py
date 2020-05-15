import itertools
s = tuple(input())
tmp = 0
for num in itertools.permutations(sorted(s, reverse=True)):
    if num > s:
        tmp = num
print(''.join(tmp) if tmp != 0 else tmp)