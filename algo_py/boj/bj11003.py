import io
import os
import sys
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    _, l = map(int, input().split())
    num = list(map(int, input().split()))
    q = deque()
    for idx, val in enumerate(num):
        while q and q[0][1]+l <= idx:
            q.popleft()
        while q and q[-1][0] >= val:
            q.pop()
        q.append((val, idx))
        sys.stdout.write(str(q[0][0])+' ')


if __name__ == '__main__':
    solve()
