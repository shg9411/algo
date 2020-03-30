import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        minTree[node] = maxTree[node] = base[s]
        return
    m = (s+e)//2
    init(node*2, s, m)
    init(node*2+1, m+1, e)
    minTree[node] = min(minTree[node*2], minTree[node*2+1])
    maxTree[node] = max(maxTree[node*2], maxTree[node*2+1])
    return


def getValue(node, s, e, l, r):
    if l > e or r < s:
        return sys.maxsize, -sys.maxsize
    if l <= s and e <= r:
        return minTree[node], maxTree[node]
    m = (s+e)//2
    lt = getValue(node*2, s, m, l, r)
    rt = getValue(node*2+1, m+1, e, l, r)
    return min(lt[0], rt[0]), max(lt[1], rt[1])


'''
def update(node, s, e, idx, diff):
    if idx < s or idx > e:
        return
    tree[node] += diff
    if s != e:
        m = (s+e)//2
        update(node*2, s, m, idx, diff)
        update(node*2+1, m+1, e, idx, diff)
'''


N, M = map(int, input().split())
base = [int(input()) for _ in range(N)]
minTree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
maxTree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
init(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*getValue(1, 0, N-1, a-1, b-1))
