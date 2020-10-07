import sys
import heapq
input = sys.stdin.readline
def solve():
    n = int(input())
    q = []
    res = []
    for _ in range(n):
        a = int(input())
        if a:
            heapq.heappush(q, (abs(a), str(a)))
        else:
            res.append(heapq.heappop(q)[1] if q else '0')
    print('\n'.join(res))

if __name__=='__main__':
    solve()
