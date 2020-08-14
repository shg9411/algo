from collections import defaultdict
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
AB = defaultdict(int)
CD = dict()
for i in range(n):
    for j in range(n):
        ab = A[i]+B[j]
        AB[ab] += 1
ans = 0
for i in range(n):
    for j in range(n):
        ans += AB[-C[i]-D[j]]
print(ans)