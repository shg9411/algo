import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        seg_tree[node] = array[s]
        return seg_tree[node]
    mid = (s+e)//2
    seg_tree[node] = init(node*2, s, mid)+init(node*2+1, mid+1, e)
    return seg_tree[node]


def query(node, s, e, left, right):
    if s > right or e < left:
        return 0
    if left <= s and e <= right:
        return seg_tree[node]
    mid = (s+e)//2
    left_query = query(node*2, s, mid, left, right)
    right_query = query(node*2+1, mid+1, e, left, right)
    return left_query+right_query


N = int(input())
H = math.ceil(math.log2(N))
size = 2**(H+1)
array = list(map(int, input().split()))
seg_tree = [0 for _ in range(size)]
init(1, 0, N-1)
res = []
for i in range(N):
    for j in range(i+1, N):
        if query(1, 0, N-1, i, j) == 0:
            res.append((i, j))
            break
c = 0
if res:
    s = 0
    e = 0
    for r in res:
        if r[0] < e:
            s = r[0]
            e = min(e, r[1])
            continue
        s = r[0]
        e = r[1]
        c += 1
print(c)
