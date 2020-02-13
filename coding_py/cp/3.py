def solution(r, delivery):
    selected = [[False for _ in range(r)] for _ in range(r)]
    time = [[0 for _ in range(r)] for _ in range(r)]
    tip = [[0 for _ in range(r)] for _ in range(r)]
    now = 0
    for i in range(r**2):
        time[i//r][i % r] = delivery[i][0]
        tip[i//r][i % r] = delivery[i][1]
    answer = 0
    tmp = [0, tip[0][0], [0, 0]]
    while 1:
        x, y = tmp[2][0], tmp[2][1]
        selected[x][y] = True
        answer += tmp[1]
        now = tmp[0]
        tmpDist = [[0 for _ in range(r)] for _ in range(r)]
        tmp = []
        for i in range(r):
            for j in range(r):
                if selected[i][j]:
                    continue
                tmpDist[i][j] = abs(x-i)+abs(y-j)
                if now+tmpDist[i][j] <= time[i][j]:
                    tmp.append([now+tmpDist[i][j], tip[i][j], [i, j]])
        if not tmp:
            break
        tmp = sorted(
            sorted(tmp, key=lambda k: k[0]), key=lambda k: k[1], reverse=True)
        tmp = tmp[0]
        if x < tmp[2][0]:
            while x+1 < tmp[2][0]:
                x += 1
                if not selected[x][y]:
                    selected[x][y] = True
                    answer += tip[x][y]
        elif x > tmp[2][0]:
            while x-1 > tmp[2][0]:
                x -= 1
                if not selected[x][y]:
                    selected[x][y] = True
                    answer += tip[x][y]
        if y < tmp[2][1]:
            while y+1 < tmp[2][1]:
                y += 1
                if not selected[x][y]:
                    selected[x][y] = True
                    answer += tip[x][y]

        elif y > tmp[2][1]:
            while y-1 > tmp[2][1]:
                y -= 1
                if not selected[x][y]:
                    selected[x][y] = True
                    answer += tip[x][y]

    return answer


delivery = [[1, 10], [8, 1], [8, 1], [3, 100], [8, 1], [8, 1], [8, 1], [
    8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [9, 100], [8, 1], [8, 1], [8, 1]]
print(solution(4, delivery))
