import sys
import heapq as hq
input = sys.stdin.readline


def solve():
    def getRecommend(x):
        if x == 1:
            while -maxH[0][1] in solved or -maxH[0][0] != problem_set[-maxH[0][1]]:
                hq.heappop(maxH)
            res.append(-maxH[0][1])
        else:
            while minH[0][1] in solved or minH[0][0] != problem_set[minH[0][1]]:
                hq.heappop(minH)
            res.append(minH[0][1])

    maxH = []
    minH = []
    solved = set()
    problem_set = {}
    res = []
    for _ in range(int(input())):
        num, level = map(int, input().split())
        problem_set[num] = level
        minH.append((level, num))
        maxH.append((-level, -num))

    hq.heapify(maxH)
    hq.heapify(minH)

    for _ in range(int(input())):
        cmd, *etc = input().split()
        if cmd[0] == 'a':
            num, level = map(int, etc)
            problem_set[num] = level
            hq.heappush(minH, (level, num))
            hq.heappush(maxH, (-level, -num))
        elif cmd[0] == 's':
            solved.add(int(etc[0]))
        else:
            getRecommend(int(etc[0]))
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    solve()
