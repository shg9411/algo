import sys

n = int(sys.stdin.readline())
girl = [sys.stdin.readline().rstrip() for _ in range(n)]
k = int(sys.stdin.readline())

if k == 1:
    print('\n'.join(girl))
elif k == 2:
    print('\n'.join(i[::-1] for i in girl))
elif k == 3:
    print('\n'.join(girl[::-1]))
