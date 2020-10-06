import sys
import heapq
input = sys.stdin.readline
def solve():
    n = int(input())
    q = []
    res = []
    for _ in range(n):
        a = int(input())
        if a != 0:
            heapq.heappush(q, (abs(a), a))
        else:
            res.append(heapq.heappop(q)[1] if q else 0)
    print('\n'.join(str(i) for i in res))

if __name__=='__main__':
    solve()
