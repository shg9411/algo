import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    tmp = input().rstrip()[1:-1]
    num = deque(map(int, tmp.split(','))) if tmp != '' else deque()
    ok = True
    rev = False
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:
            try:
                if not rev:
                    num.popleft()
                else:
                    num.pop()
            except:
                ok = False
                break
    if not ok:
        print('error')
    else:
        print('[', end='')
        if rev:
            num.reverse()
        print(','.join(map(str, num)), end=']\n')
