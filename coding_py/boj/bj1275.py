import math
import sys
input = sys.stdin.readline


def init(arr, tree, node, s, e):
    #print(node, s, e)
    if s == e:
        tree[node] = arr[s]
        return tree[node]

    m = (s+e)//2
    tree[node] = init(arr, tree, node*2, s, m) + \
        init(arr, tree, node*2+1, m+1, e)
    return tree[node]


def update(tree, node, s, e, idx, diff):
    if not s <= idx <= e:
        return

    tree[node] += diff
    if s != e:
        mid = (s+e)//2
        update(tree, node*2, s, mid, idx, diff)
        update(tree, node*2+1, mid+1, e, idx, diff)


def getValue(tree, node, s, e, left, right):
    if left > e or right < s:
        return 0
    if left <= s and e <= right:
        return tree[node]

    mid = (s+e)//2
    return getValue(tree, node*2, s, mid, left, right)+getValue(tree, node*2+1, mid+1, e, left, right)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0 for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(arr, tree, 1, 0, n-1)
# print(tree)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(getValue(tree, 1, 0, n-1, x-1, y-1))
    diff = b-arr[a-1]
    arr[a-1] = b
    update(tree, 1, 0, n-1, a-1, diff)
