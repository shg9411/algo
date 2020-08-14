from functools import cmp_to_key
input()
tmp = ''.join(sorted(input().split(), key=cmp_to_key(
    lambda x, y: 1 if x+y < y+x else -1)))
print(tmp if tmp[0] != '0' else '0')