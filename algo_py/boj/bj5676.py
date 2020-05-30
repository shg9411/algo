import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        seg_tree[node] = array[s]
        return seg_tree[node]
    mid = (s+e)//2
    seg_tree[node] = init(node*2, s, mid)*init(node*2+1, mid+1, e)
    return seg_tree[node]


def query(node, s, e, left, right):
    if s > right or e < left:
        return 1
    if left <= s and e <= right:
        return seg_tree[node]
    mid = (s+e)//2
    left_query = query(node*2, s, mid, left, right)
    right_query = query(node*2+1, mid+1, e, left, right)
    return left_query*right_query


def update(node, s, e, idx, val):
    if idx < s or idx > e:
        return seg_tree[node]

    if s == e:
        seg_tree[node] = val
        return seg_tree[node]

    mid = (s+e)//2
    left_val = update(node*2, s, mid, idx, val)
    right_val = update(node*2+1, mid+1, e, idx, val)
    seg_tree[node] = left_val*right_val
    return seg_tree[node]


if __name__ == '__main__':
    while 1:
        try:
            N, K = map(int, input().split())
        except:
            break
        H = math.ceil(math.log2(N))
        size = 2**(H+1)
        array = [1]+list(map(int, input().split()))
        for num in map(int, input().split()):
            if num > 0:
                array.append(1)
            elif num == 0:
                array.append(0)
            else:
                array.append(-1)

        seg_tree = [0 for _ in range(size)]
        res = []
        init(1, 1, N)
        for _ in range(K):
            q, i, V = input().split()
            i, V = int(i), int(V)
            if q == 'C':
                if V > 0:
                    V = 1
                elif V == 0:
                    V = 0
                else:
                    V = -1
                update(1, 1, N, i, V)
            else:
                val = query(1, 1, N, i, V)
                if val > 0:
                    res.append('+')
                elif val == 0:
                    res.append('0')
                else:
                    res.append('-')
        print(''.join(res))
