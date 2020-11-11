import heapq
import sys
input = sys.stdin.readline


def solve():
    q = []
    res = 0
    for s, e in sorted([tuple(map(int, input().split())) for _ in range(int(input()))]):
        if not q or q[0] > s:
            res += 1
        else:
            heapq.heappop(q)
        heapq.heappush(q, e)
    print(res)


if __name__ == '__main__':
    solve()