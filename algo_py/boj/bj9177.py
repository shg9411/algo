from collections import deque

t = int(input())

for i in range(1, t+1):
    a, b, c = input().split()
    visited = [[False for _ in range(len(c)+1)] for _ in range(len(c)+1)]
    can = False
    q = deque([])
    q.append([["", 0], [0, 0]])
    q.append([["", 0], [0, 0]])
    while q:
        tmp = q.popleft()
        string = tmp[0][0]
        pos = tmp[0][1]
        posA = tmp[1][0]
        posB = tmp[1][1]
        if c == string:
            can = True
            break
        if posA < len(a) and not visited[posA+1][posB] and a[posA] == c[pos]:
            q.append([[string+a[posA], pos+1], [posA+1, posB]])
            visited[posA+1][posB] = True
        if posB < len(b) and not visited[posA][posB+1] and b[posB] == c[pos]:
            q.append([[string+b[posB], pos+1], [posA, posB+1]])
            visited[posA][posB+1] = True

    print('Data set {}: {}'.format(i, 'yes' if can else 'no'))
