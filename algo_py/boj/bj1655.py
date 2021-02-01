import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
import heapq


def solve():
    max_q = []
    min_q = []
    for _ in range(int(input())):
        num = int(input())
        if not max_q or len(max_q) == len(min_q):
            heapq.heappush(max_q, -num)
        else:
            heapq.heappush(min_q, num)

        if max_q and min_q and -max_q[0] > min_q[0]:
            heapq.heappush(min_q, -heapq.heappop(max_q))
            heapq.heappush(max_q, -heapq.heappop(min_q))
        print(-max_q[0])


if __name__ == '__main__':
    solve()