import sys
import bisect
input = sys.stdin.readline

n, m, k = map(int, input().split())
card = sorted(list(map(int, input().split())))
used = [False for _ in range(m)]
chulsu = list(map(int, input().split()))

for i in range(k):
    tmp = bisect.bisect_right(card,chulsu[i])
    for j in range(tmp,m):
        if not used[j] and card[j]>chulsu[i]:
            print(card[j])
            used[j] = True
            break
