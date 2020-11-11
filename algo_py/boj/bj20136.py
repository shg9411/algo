import heapq
from collections import deque


def solve():
    n, k = map(int, input().split())
    l = [deque() for _ in range(k+1)]
    using = [0]*(k+1)
    use = list(map(int, input().split()))
    for idx, v in enumerate(use, start=1):
        l[v].append(idx)
    pq, dq, ans, cur = [], [], 0, 0
    for item in use:
        if not using[item]:
            while pq and dq and pq[0] == dq[0]:
                heapq.heappop(pq)
                heapq.heappop(dq)
            if cur == n:
                using[pq[0][1]] = 0
                heapq.heappop(pq)
                cur -= 1
                ans += 1
            l[item].popleft()
            if not l[item]:
                heapq.heappush(pq, (-k-1, item))
            else:
                heapq.heappush(pq, (-l[item][0], item))
            using[item] = 1
            cur += 1
        else:
            heapq.heappush(dq, (-l[item].popleft(), item))
            if not l[item]:
                heapq.heappush(pq, (-k-1, item))
            else:
                heapq.heappush(pq, (-l[item][0], item))
    print(ans)


if __name__ == '__main__':
    solve()
