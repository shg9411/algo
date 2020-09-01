import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

score = [list(map(int, input().split())) for _ in range(n)]

selected = [False for _ in range(n)]

minV = 1000000


def calc():
    global minV
    ls = [i for i, v in enumerate(selected) if v == False]
    ss = [i for i, v in enumerate(selected) if v == True]
    tmps = 0
    tmpl = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            si = ss[i]
            sj = ss[j]
            li = ls[i]
            lj = ls[j]
            tmps += (score[si][sj]+score[sj][si])
            tmpl += (score[li][lj]+score[lj][li])
    minV = min(minV, abs(tmps-tmpl))


def select(count, idx):
    if count == n//2:
        calc()
        return
    for i in range(idx, n):
        # if not selected[i]:
        selected[i] = True
        select(count+1, i+1)
        selected[i] = False


select(0, 0)
print(minV)
