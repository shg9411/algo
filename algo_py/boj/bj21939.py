import sys
import heapq
input = sys.stdin.readline


def getRecommend(x):
    if x == 1:
        while -max_heap[0][1] in solved or -max_heap[0][0] != problem_set[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        print(-max_heap[0][1])
    else:
        while min_heap[0][1] in solved or min_heap[0][0] != problem_set[min_heap[0][1]]:
            heapq.heappop(min_heap)
        print(min_heap[0][1])


max_heap = []
min_heap = []
solved = set()
problem_set = {}
for _ in range(int(input())):
    num, level = map(int, input().split())
    problem_set[num] = level
    min_heap.append((level, num))
    max_heap.append((-level, -num))

heapq.heapify(max_heap)
heapq.heapify(min_heap)


for _ in range(int(input())):
    cmd, *etc = input().split()
    if cmd[0] == 'a':
        num, level = map(int, etc)
        problem_set[num] = level
        heapq.heappush(min_heap, (level, num))
        heapq.heappush(max_heap, (-level, -num))
    elif cmd[0] == 's':
        solved.add(int(etc[0]))
    else:
        getRecommend(int(etc[0]))
