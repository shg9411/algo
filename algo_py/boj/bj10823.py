import sys
s = ''
for tmp in sys.stdin.read().split():
    s+=tmp
print(sum(map(int,s.split(','))))