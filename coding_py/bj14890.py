import sys
input = sys.stdin.readline

n, l = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    same = 1
    curr = m[i][0]
    ok = True
    for j in range(1, n):
        if m[i][j] != curr:
            if m[i][j] == curr+1 and same == l:
                same = 1
                curr = m[i][j]
                continue
            if m[i][j] == curr-1 and same == l:
                same = 1
                curr = m[i][j]
                continue
            ok = False
            break
        else:
            same += 1
    if ok:
        count += 1
        print(i)

# print(count)
