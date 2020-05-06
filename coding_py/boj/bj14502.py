from collections import deque

lab, list_virus = [], []
N, M, NxM, maximum, origin_0_count, num_virus = 0, 0, 0, 0, 0, 0

def spread(queue) : # 전염시킬수 있는 영역 계산.
    count = 0
    while(queue) : # not empty
        virus = queue.popleft()
        x, y = virus//M, virus%M
        count+=1
        if x+1 < N and lab[x+1][y] == 0 : 
            lab[x+1][y] = 3
            queue.append(virus+M)
        if x-1 > -1 and lab[x-1][y] == 0 : 
            lab[x-1][y] = 3
            queue.append(virus-M)
        if y+1 < M and lab[x][y+1] == 0 : 
            lab[x][y+1] = 3
            queue.append(virus+1)
        if y-1 > -1 and lab[x][y-1] == 0 : 
            lab[x][y-1] = 3
            queue.append(virus-1)

    for i in range(0, N) :
        for j in range(0, M) :
            if (lab[i][j] == 3) :
                lab[i][j] = 0
    return count

def check() : # 안전 구역 개수 세기
    queue = deque(list_virus)
    spreaded_count = spread(queue) - num_virus
    return (origin_0_count-3)-spreaded_count

def DFS(count, index) : # count = 사용한 벽 개수, index = 현재 매트릭스에서의 index
    if count == 3 :
        local = check()
        global maximum
        maximum = max(maximum, local)
        return
    if index == NxM :
        return
    for curr in range(index, NxM) :
        x, y = curr//M, curr%M
        if lab[x][y] != 0 :
            continue
        lab[x][y] = 1
        DFS(count+1, curr+1)
        lab[x][y] = 0
    
if __name__=='__main__' :
    N_M = [int(x) for x in input().split(' ')]
    N, M = N_M[0], N_M[1]
    NxM = N*M
    count = 0
    for i in range(0, N) :
        temp = [int(x) for x in input().split(' ')]
        lab.append(temp)
        
        for j in range(0 ,M) :
            if temp[j] != 0 :
                count += 1
                if temp[j] == 2 :
                    viurs = i*M + j
                    list_virus.append(viurs)    
    
    num_virus = len(list_virus)
    origin_0_count = NxM - count
    DFS(0, 0)
    print(maximum)