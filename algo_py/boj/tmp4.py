import heapq


def solution(N, coffee_times):
    cur = 0
    answer = []
    robot = []
    for idx, time in enumerate(coffee_times, start=1):
        if len(robot) < N:
            heapq.heappush(robot, (cur+time, idx))
        else:
            cur, index = heapq.heappop(robot)
            answer.append(index)
            heapq.heappush(robot, (cur+time, idx))
    while robot:
        answer.append(heapq.heappop(robot)[1])
    return answer


N = 1
coffee_times = [100, 1, 50, 1, 1]
print(solution(N, coffee_times))
