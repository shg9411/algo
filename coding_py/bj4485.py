import sys
import heapq
input = sys.stdin.readline
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]
a = 1
while a:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    dist[0][0] = cave[0][0]
    q = [[cave[0][0],0,0]]
    while q:
        dis,x,y = heapq.heappop(q)
        if x==n-1 and y==n-1:
            print('Problem {}: {}'.format(a,dis))
            a+=1
            break
        if dis > dist[x][y]:
            continue
        for [nx,ny] in nm:
            tx = x+nx
            ty = y+ny
            if 0<=tx<n and 0<=ty<n:
                tmp = dis+cave[tx][ty]
                if tmp < dist[tx][ty]:
                    dist[tx][ty] = tmp
                    heapq.heappush(q,[tmp,tx,ty])
    
