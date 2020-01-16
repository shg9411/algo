import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chicken = []
house = []
selected = []
city = [[] for _ in range(n)]
minV = 100*n


#입력받으면서 치킨집과 집의 좌표 저장
for i in range(n):
    city[i] = list(map(int, input().split()))
    for idx, val in enumerate(city[i]):
        if val == 1:
            house.append([i, idx])
        elif val == 2:
            chicken.append([i, idx])
            selected.append(False)

#집에서 치킨집의 거리를 저장하기 위한 리스트 생성
distance = [[0 for _ in range(len(chicken))] for _ in range(len(house))]


#조합마다 거리 계산
def getDistance():
    global minV
    total = 0
    #각 집마다 가장 가까운 치킨집 거리 계산
    for i in range(len(house)):
        tmp = 100
        for j in range(len(selected)):
            #선택되었고
            if selected[j]:
                #거리를 계산한적이 없으면 계산
                if not distance[i][j]:
                    distance[i][j] = abs(house[i][0]-chicken[j][0]) + \
                        abs(house[i][1]-chicken[j][1])
                #계산했었으면 저장된 값 사용
                tmp = min(tmp, distance[i][j])
        #가장 가까운 치킨집까지의 거리 더함
        total += tmp
    minV = min(total, minV)


#치킨집 m개만큼 남겨둠
def getChicken(idx, count):
    if count == m:
        getDistance()
        return

    for i in range(idx, len(chicken)):
        if not selected[i]:
            selected[i] = True
            getChicken(i+1, count+1)
            selected[i] = False


getChicken(0, 0)
print(minV)
