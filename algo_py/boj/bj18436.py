import math
import sys
input = sys.stdin.readline


def init(arr, tree, node, s, e):
    if s == e:
        tree[node] = 1 if arr[s] % 2 == 1 else 0
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


n = int(input())
arr = [0 if i % 2 == 0 else 1 for i in map(int, input().split())]
tree = [0 for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(arr, tree, 1, 0, n-1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        if c % 2 == 1 and arr[b-1] == 0:
            update(tree, 1, 0, n-1, b-1, 1)
        elif c % 2 == 0 and arr[b-1] == 1:
            update(tree, 1, 0, n-1, b-1, -1)
        arr[b-1] = c % 2
    else:
        val = getValue(tree, 1, 0, n-1, b-1, c-1)
        if a == 2:
            print(c-b+1-val)
        else:
            print(val)
