dx = [0,1,0,-1]
dy = [1,0,-1,0]

def change(d, c):
    if(c == "L"):
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d
        
def start():
    cnt = 0
    # 뱀 위치 표시
    x = 0
    y = 0
    arr[x][y] = 3
    d = 0
    idx = 0
    # 뱀의 꼬리 ~ 머리까지의 정보를 q에 담기
    q = []
    q.append((x,y))
    while(True):
        # 몇초에 방향 전환 하는지
        if(game[idx][0] == cnt):
            d = change(d, game[idx][1])
            idx += 1
        print(q)
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위안에 있고, 자기자신이 아니라면
        if(0<=nx<n and 0<=ny<n and arr[nx][ny] != 3):
            # 사과를 먹으면 꼬리는 그대로
            if(arr[nx][ny] == 1):
                arr[nx][ny] = 3
                q.append((nx,ny))
            # 사과를 못먹으면 꼬리 하나 떼기
            elif(arr[nx][ny] == 0):
                arr[nx][ny] = 3
                q.append((nx,ny))
                tx, ty = q.pop(0)
                arr[tx][ty] = 0
            x = nx
            y = ny
            cnt += 1
        else:
            cnt += 1
            break
    return cnt

n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
l = int(input())
game = [[0,0]]*10000
for i in range(l):
    x, c = input().split()
    game[i] = [int(x), c]
res = start()
print(res)