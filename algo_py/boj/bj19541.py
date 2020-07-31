import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meeting = [list(map(int, input().split()))[1:] for _ in range(m)]
status = [0]+list(map(int, input().split()))
res = status[:]

#역학조사
for meet in meeting[::-1]:
    covid = True
    #모임에 있던 사람들 중 걸리지 않은 사람이 있다면 그 모임 할 당시에 감염자는 없음
    for people in meet:
        if status[people] == 0:
            covid = False
            break
    #따라서 초기 감염자 목록에서 제외
    if not covid:
        for people in meet:
            status[people] = 0

#초기 감염자 후보
tmpCandi = status[:][1:]

#후보들을 대상으로 시뮬레이션 진행
for meet in meeting:
    covid = False
    for people in meet:
        if status[people] == 1:
            covid = True
            break
    if covid:
        for people in meet:
            status[people] = 1

for i in range(1, n+1):
    if status[i] != res[i]:
        print("NO")
        exit()
print("YES")
print(' '.join(map(str, tmpCandi)))