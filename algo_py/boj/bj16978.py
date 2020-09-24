import sys
import math
from collections import deque
input = sys.stdin.readline


def solve():
    def init(a, node, s, e):
        if s == e:
            tree[node] = base[s]
            return tree[node]
        m = (s+e)//2
        tree[node] = init(base, node*2, s, m) + \
            init(base, node*2+1, m+1, e)
        return tree[node]

    def sum(node, s, e, l, r):
        if l > e or r < s:
            return 0
        if l <= s and e <= r:
            return tree[node]
        m = (s+e)//2
        return sum(node*2, s, m, l, r)+sum(node*2+1, m+1, e, l, r)

    def update(node, s, e, idx, diff):
        if idx < s or idx > e:
            return
        tree[node] += diff
        if s != e:
            m = (s+e)//2
            update(node*2, s, m, idx, diff)
            update(node*2+1, m+1, e, idx, diff)

    N = int(input())
    base = list(map(int, input().split()))
    tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
    init(base, 1, 0, N-1)
    M = int(input())
    tmp1 = []
    tmp2 = []
    i = 0
    for _ in range(M):
        a, b, *c = map(int, input().split())
        if a == 1:
            tmp1.append([b, c[0]])
        else:
            tmp2.append([b, c[0], c[1], i])
            i += 1
    tmp2.sort()
    tmp1 = deque(tmp1)
    res = [0 for _ in range(len(tmp2))]
    i = 0
    for a, b, c, d in tmp2:
        while i < a and tmp1:
            x, y = tmp1.popleft()
            diff = y-base[x-1]
            base[x-1] = y
            update(1, 0, N-1, x-1, diff)
            i += 1
        res[d] = str(sum(1, 0, N-1, b-1, c-1))
    print('\n'.join(res))


if __name__ == "__main__":
    solve()
