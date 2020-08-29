'''
문제 설명
복잡한 연산을 빠르게 처리하기 위해 연산을 N개로 나누어 병렬적으로 처리하기로 하였습니다. 연산에는 이전 단계의 계산 값이 나와야만 다음 단계가 가능한 연산과, 동시에 진행해도 상관없는 연산이 있으므로 병렬 프로그래밍으로 연산을 처리하면 훨씬 일을 빠르게 처리할 수 있습니다. 각 연산별 수행시간 리스트 T, 종속되어 있는 연산들의 관계 R이 주어집니다. N개로 나눈 연산을 각각 1,2,3,...,K,...N번 연산이라고 할 때, K번 연산이 가장 빨리 끝나는 시점을 반환하는 함수를 완성해 주세요.

제한사항
수행시간 리스트 T의 각 원소는 1,000 이하의 자연수로 이루어져 있습니다. (각 원소는 1번 연산, 2번 연산...N번 연산의 수행 시간을 의미합니다.)
수행시간 리스트 T의 원소 개수 N은 2 이상 1,000 이하의 자연수 입니다.
연산들의 관계 R의 각 원소는 [Si, Ei] 로 이루어져 있으며, Si번째 연산이 끝나야 Ei번째 연산을 할 수 있다는 의미입니다. (단, Si와 Ei는 같지 않고, 1보다 크거나 같고, T보다 작거나 같은 자연수입니다.)
연산들의 관계 R의 원소 개수는 200,000 이하의 자연수 입니다.
K번 연산은 리스트 T의 원소 개수 N보다 작거나 같은 자연수입니다.
'''

from collections import deque


def solution(T, R, k):
    n = len(T)
    time = [0]+T
    res = [0 for _ in range(n+1)]
    num = [0 for _ in range(n+1)]
    after = [[] for _ in range(n+1)]
    for i, j in R:
        after[i].append(j)
        num[j] += 1
    q = deque()
    for i in range(1, n+1):
        if num[i] == 0:
            q.append(i)
    for _ in range(n):
        tmp = q.popleft()
        res[tmp] += time[tmp]
        if tmp == k:
            return res[k]
        for a in after[tmp]:
            res[a] = max(res[a], res[tmp])
            if num[a] == 1:
                q.append(a)
            num[a] -= 1
    return


T = [5, 8, 3, 7, 10, 5, 4]
R = [[1, 2], [2, 4], [1, 4], [6, 5], [3, 5], [4, 6]]
K = 5
print(solution(T, R, K))

'''
q = deque()
for i in range(1, n+1):
    if num[i] == 0:
        q.append(i)
for _ in range(n):
    tmp = q.popleft()
    res[tmp] += time[tmp]
    for a in after[tmp]:
        res[a] = max(res[a], res[tmp])
        if num[a] == 1:
            q.append(a)
        num[a] -= 1
        '''
