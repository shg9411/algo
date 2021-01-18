import sys
num = []
for l in sys.stdin:
    num.extend(map(lambda x: int(x[::-1]), l.split()))
print('\n'.join(map(str, sorted(num[1:]))))
