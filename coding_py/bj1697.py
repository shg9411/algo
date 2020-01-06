n, k = map(int, input().split())

sumba = [0] * 100001


def bfs(i, j):
    sumba[i] = 1
    q = [i]
    while q:
        tmp = q.pop(0)
        if tmp == j:
            break
        if tmp < 100000 and sumba[tmp+1] == 0:
            q.append(tmp+1)
            sumba[tmp+1] = sumba[tmp]+1
        if tmp > 0 and sumba[tmp-1] == 0:
            q.append(tmp-1)
            sumba[tmp-1] = sumba[tmp] + 1
        if tmp * 2 < 100001 and sumba[tmp*2] == 0:
            q.append(tmp*2)
            sumba[tmp*2] = sumba[tmp]+1

    print(sumba[j]-1)


bfs(n, k)
