import sys
from collections import deque
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()
#sys.stdin = open('inputs/boj/7576_input')


def solution(graph, queue):
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 혹시 모를 visited 행렬 구현
    visited = [[0 for _ in range(m)] for _ in range(n)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                visited[nr][nc] = visited[r][c] + 1
                queue.append(tuple([nr, nc]))

    if 0 in graph:
        return -1
    else:
        return max(max(visited))


if __name__ == '__main__':
    m, n = map(int, input().split())
    farm = []
    queue = deque()
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 1:
                # 1인 경우에 큐에 넣어준다.
                queue.append(tuple([i, j]))

        farm.append(line)

    result = solution(farm, queue)
    print(result)
