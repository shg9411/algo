import bisect as b
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    q = deque()
    pd = dict()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'I':
            val = int(cmd[1])
            if val not in pd:
                b.insort_left(q, val)
                pd[val] = 1
            else:
                pd[val] += 1
        else:
            if not q:
                continue
            if cmd[1] == '1':
                if (v := pd[q[-1]]) > 1:
                    pd[q[-1]] = v-1
                else:
                    pd.pop(q[-1])
                    q.pop()
            else:
                if (v := pd[q[0]]) > 1:
                    pd[q[0]] = v-1
                else:
                    pd.pop(q[0])
                    q.popleft()
    if q:
        print(q[-1], q[0])
    else:
        print("EMPTY")


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
