r, c = map(int, input().split())
myMap = []
result = 1
myAlpha = dict()

def check(nx, ny):
    global result
    
    if myMap[nx][ny] not in myAlpha:
        myAlpha[myMap[nx][ny]] = 1 #해당 알바펫을(key) 추가
        print(myAlpha)
        result += 1
        return True
    else:
        return False
    
    
def Alpha(x, y):
    queue = list()
    queue.append((x, y))
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    myAlpha[myMap[x][y]] = 1
    
    while queue:
        x, y = queue.pop(0)
#         print(x, y)
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
    
            if check(nx, ny):
                queue.append((nx, ny))
                
              
    
for _ in range(r):
    string = input()
    myMap.append(string)
    
    
Alpha(0, 0)
print(result)