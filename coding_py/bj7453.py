import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB = dict()
CD = dict()
for i in range(n):
    for j in range(n):
        ab = A[i]+B[j]
        cd = C[i]+D[j]
        try:
            AB[ab] += 1
        except:
            AB[ab] = 1
        try:
            CD[cd] += 1
        except:
            CD[cd] = 1

ans = 0
for idx, val in enumerate(AB):
    try:
        ans += AB[val]*CD[-val]
    except:
        continue
print(ans)
