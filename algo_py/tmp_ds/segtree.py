import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    # node가 leaf node일 경우 자신의 값을 넣고 반환
    if s == e:
        seg_tree[node] = array[s]
        return seg_tree[node]
    # leaf node가 아닐 경우 왼쪽 자식과 오른쪽 자식의 합을 넣고 반환
    mid = (s+e)//2
    seg_tree[node] = init(node*2, s, mid)+init(node*2+1, mid+1, e)
    return seg_tree[node]


# 기본형이므로 sum을 구현
# s,e는 node의 담당 구간, left,right는 쿼리에서 주어진 구간
def query(node, s, e, left, right):
    # 담당 구간이 아닌 경우 0 반환
    if s > right or e < left:
        return 0
    # 구간에 완벽히 포함되어 있을 때 node 값 반환
    if left <= s and e <= right:
        return seg_tree[node]
    # 이외의 상황에서는 왼쪽 자식과 오른쪽 자식으로 나눠서 탐색해야 함
    mid = (s+e)//2
    left_query = query(node*2, s, mid, left, right)
    right_query = query(node*2+1, mid+1, e, left, right)
    return left_query+right_query


# 수의 변경이 일어나면 그 노드가 포함된 구간을 모두 업데이트 해줘야 함
def update(node, s, e, idx, diff):
    # 노드 담당 구간이 아닌 경우 return
    if idx < s or idx > e:
        return
    # 담당 구간인 경우 diff(원래 값과 변경 값만큼의 차이)를 더해주고 자식들도 업데이트
    seg_tree[node] += diff
    if s != e:
        mid = (s+e)//2
        update(node*2, s, mid, idx, diff)
        update(node*2+1, mid+1, e, idx, diff)


N, M, Q = map(int, input().split())
# 트리의 높이
H = math.ceil(math.log2(N))
# 트리 사이즈
size = 2**(H+1)-1
# 값들이 있는 기본 배열
array = [int(input()) for _ in range(N)]
# 세그먼트 트리
seg_tree = [0 for _ in range(size)]
init(1, 0, N-1)
for _ in range(M+Q):
    q, a, b = map(int, input().split())
    if q == 1:
        diff = b-array[a-1]
        array[a-1] = b
        update(1, 0, N-1, a-1, diff)
    else:
        print(query(1, 0, N-1, a-1, b-1))
