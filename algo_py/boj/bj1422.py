import sys
import functools
input = sys.stdin.readline


def compare(a, b):
    if len(a) != len(b):
        return len(a)-len(b)
    return int(a)-int(b)


K, N = map(int, input().split())
num = sorted([input().rstrip() for _ in range(K)],
             key=functools.cmp_to_key(compare))
for i in range(N-K):
    num.append(num[-1])
num.sort(key=functools.cmp_to_key(
    lambda x, y: 1 if int(x+y) > int(y+x) else -1))
print(''.join(num[::-1]))
