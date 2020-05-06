import sys
n, m = map(int, input().split())
person = sys.stdin.read().splitlines()
hear = set(person[:n])
see = set(person[n:])
ret = list(hear & see)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
