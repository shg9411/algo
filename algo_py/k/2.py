from collections import deque


def solve(place):
    people = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
    for person in people:
        tmp = [place[i][:] for i in range(5)]
        visit = [[0]*5 for _ in range(5)]
        q = deque([person])
        visit[person[0]][person[1]] = 1
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for _i, _j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ti, tj = i+_i, j+_j
                    if 0 <= ti < 5 and 0 <= tj < 5 and not visit[ti][tj] and tmp[ti][tj] != 'X':
                        if dist<=2 and tmp[ti][tj]=='P':
                            return 0
                        visit[ti][tj] = 1
                        q.append((ti, tj))

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(solve(place))
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
