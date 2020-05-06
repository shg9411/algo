import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = base[s]
        #minTree[node] = base[s]
        #maxTree[node] = base[s]
        return
    m = (s+e)//2
    init(node*2, s, m)
    init(node*2+1, m+1, e)

    #minTree[node] = min(minTree[node*2], minTree[node*2+1])
    #maxTree[node] = max(maxTree[node*2], maxTree[node*2+1])
    return


'''
def getMax(node, s, e, l, r):
    if l > e or r < s:
        return -sys.maxsize
    if l <= s and e <= r:
        return maxTree[node]
    m = (s+e)//2
    return max(getMax(node*2, s, m, l, r), getMax(node*2+1, m+1, e, l, r))


def getMin(node, s, e, l, r):
    if l > e or r < s:
        return sys.maxsize
    if l <= s and e <= r:
        return minTree[node]
    m = (s+e)//2
    return min(getMin(node*2, s, m, l, r), getMin(node*2+1, m+1, e, l, r))
'''


def update(node, s, e, idx, diff):
    if idx < s or idx > e:
        return
    tree[node] += diff
    if s != e:
        m = (s+e)//2
        update(node*2, s, m, idx, diff)
        update(node*2+1, m+1, e, idx, diff)


N, M = map(int, input().split())
base = [int(input()) for _ in range(N)]
tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
#minTree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
#maxTree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
init(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    #print(getMin(1, 0, N-1, a-1, b-1), getMax(1, 0, N-1, a-1, b-1))
