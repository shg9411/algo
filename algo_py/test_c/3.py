from collections import deque
import heapq


def solution(customer, K):
    status = dict()
    for i, [idx, cmd] in enumerate(customer):
        if cmd == 0:
            status[idx].popleft()
        else:
            try:
                status[idx].append(i)
            except:
                status[idx] = deque([i])
    tmp = []
    for idx, state in status.items():
        if state:
            heapq.heappush(tmp, (state.popleft(), idx))
    cnt = 0
    answer = []
    while cnt < K and tmp:
        answer.append(heapq.heappop(tmp)[1])
        cnt += 1
    return sorted(answer)


customer = [[2, 1], [1, 1], [3, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
K = 1
print(solution(customer, K))
