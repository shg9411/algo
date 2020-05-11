import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    score = list(map(int, input().split()))
    tmp = sum(score[1:])/score[0]
    cnt = 0
    for sc in score[1:]:
        if sc > tmp:
            cnt += 1
    print("%.3f%%" % (cnt/score[0]*100))
