import sys
import math
input = sys.stdin.readline
INF = 1e9+1


def init(node, s, e):
    if s == e:
        seg_tree[node] = [array[s], array[s], array[s]]
        return
    mid = (s+e)//2
    seg_tree[node] = [-INF, -INF, -INF]
    l = r = 0
    for i in range(e, s-1, -1):
        l += array[i]
        seg_tree[node][0] = max(seg_tree[node][0], l)
    for i in range(s, e+1):
        r += array[i]
        seg_tree[node][2] = max(seg_tree[node][2], r)
    init(node*2, s, mid)
    init(node*2+1, mid+1, e)
    seg_tree[node][1] = max(seg_tree[node*2][1], seg_tree[node*2+1]
                            [1], seg_tree[node*2][0]+seg_tree[node*2+1][2])
    return


def query(node, s, e, left, right):
    if s > right or e < left:
        return [-INF, -INF, -INF]
    if left <= s and e <= right:
        return seg_tree[node]
    mid = (s+e)//2
    left_query = query(node*2, s, mid, left, right)
    right_query = query(node*2+1, mid+1, e, left, right)
    tmp = []
    tmp.append(max(left_query[0]+summ[e]-summ[mid], right_query[0]))
    tmp.append(max(left_query[1], right_query[1],
                   left_query[0]+right_query[2]))
    tmp.append(max(left_query[2], summ[mid]-summ[s-1]+right_query[2]))
    return tmp


N = int(input())
H = math.ceil(math.log2(N))
size = 2**(H+1)
array = [0]
summ = [0]
array += list(map(int, input().split()))
for i in range(1, N+1):
    summ.append(summ[-1]+array[i])
seg_tree = [0 for _ in range(size)]
init(1, 1, N)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 1, N, a, b)[1])