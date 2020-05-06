import sys
import bisect
input = sys.stdin.readline

n, m, k = map(int, input().split())
#카드 정렬
card = sorted(list(map(int, input().split())))
#사용 여부 판별
used = [False for _ in range(m)]
chulsu = list(map(int, input().split()))

for i in range(k):
    #인덱스 확인
    tmp = bisect.bisect_right(card,chulsu[i])
    #인덱스를 증가하면서 안 사용한 카드를 출력
    for j in range(tmp,m):
        if not used[j]:
            print(card[j])
            used[j] = True
            break
