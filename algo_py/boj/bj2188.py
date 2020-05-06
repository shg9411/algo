import sys
input = sys.stdin.readline


def dfs(i):
    for want in cow[i]: #소가 원하는 축사들 중
        if check[want]: #이미 방문(검사)했으면 넘어감
            continue
        check[want] = True
        if house[want] == 0 or dfs(house[want]): #축사가 비어있거나, 축사를 선점한 소가 다른 축사에 갈 수 있을 때
            house[want] = i #축사를 소에게 배정해줌
            return True #축사에 소가 들어갔다고 반환
    return False #들어갈 자리가 없다고 반환


n, m = map(int, input().split())

cow = [[] for _ in range(n+1)] #소가 원하는 축사를 저장할 리스트
house = [0 for _ in range(m+1)] #축사에 들어있는 소를 저장할 리스트
res = 0

for i in range(1, n+1):
    cow[i].extend(list(map(int, input().split()))[1:]) #소가 원하는 축사 저장

for i in range(1, n+1):
    check = [False for _ in range(m+1)] #방문 여부 리스트
    if dfs(i):
        res += 1

print(res)
