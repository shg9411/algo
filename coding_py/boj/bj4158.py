import sys
input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())
    if n+m == 0:
        break
    sg = [int(input()) for _ in range(n)]
    sy = [int(input()) for _ in range(m)]
    i, j = 0, 0
    count = 0
    while 1:
        if i >= m or j >= n:
            break
        if sg[i] > sy[j]:
            j += 1
        elif sg[i] < sy[j]:
            i += 1
        else:
            count += 1
            i, j = i+1, j+1
    print(count)
