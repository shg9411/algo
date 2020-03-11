from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    total = 0
    while truck_weights:
        if len(bridge) < bridge_length and total+truck_weights[0] <= weight:
            current = truck_weights.popleft()
            total += current
            bridge.append([current, 0])
        for truck in bridge:
            truck[1] += 1
        while bridge:
            tmp = bridge[0]
            if tmp[1] == bridge_length:
                bridge.popleft()
                total -= tmp[0]
            else:
                break
        answer += 1
    if bridge:
        answer += (bridge_length - bridge[-1][1])
    return answer+1


n, l, w = map(int, input().split())
truck = list(map(int, input().split()))
print(solution(l, w, truck))
