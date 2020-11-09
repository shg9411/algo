import heapq
from collections import deque


def solve():
    n, k = map(int, input().split())
    pt = dict()

    class Node(object):
        def __init__(self, val: int):
            self.val = val
            pt[val] = latency[val].popleft()[1]

        def __repr__(self):
            return '{}({})'.format(self.val, pt[self.val])

        def __lt__(self, other):
            return pt[self.val] > pt[other.val]
    cur = set()
    q = []
    latency = dict()
    things = list(map(int, input().split()))
    for idx, item in enumerate(things):
        if item not in latency:
            latency[item] = deque([(idx, k)])
        else:
            lastidx, lastv = latency[item].pop()
            latency[item].append((lastidx, idx))
            latency[item].append((idx, k))
    res = 0
    for thing in things:
        if thing in cur:
            pt[thing] = latency[thing].popleft()[1]
            if pt[thing] > pt[q[0].val]:
                heapq.heapify(q)
        else:
            if len(q) == n:
                popItem = heapq.heappop(q)
                cur.remove(popItem.val)
                res += 1
            cur.add(thing)
            heapq.heappush(q, Node(thing))
    print(res)


if __name__ == '__main__':
    solve()