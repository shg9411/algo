import sys
from collections import deque
input = sys.stdin.readline


def solve():
    p = list(input().rstrip())
    n = int(input())
    res = input().rstrip()[1:-1].split(',')
    if len(res) < p.count('D') or res == [''] and p.count('D') > 0:
        print('error')
        return
    i, j = 0, 0
    rev = False
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:
            if not rev:
                i += 1
            else:
                j += 1

    res = res[i:n-j]
    print('[', end='')
    print(','.join(res[::-1] if rev else res), end=']\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
