import copy
import sys
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m_c = copy.deepcopy(m)

for k in range(len(m)):
    for i in range(len(m)):
        for j in range(len(m)):
            if i == k or j == k:
                continue
            if m[i][j] > m[i][k] + m[k][j]:
                print(-1)
                sys.exit()
            if m[i][j] == m[i][k] + m[k][j]:
                m_c[i][j] = 0

t = 0
for i in range(len(m_c)):
    for j in range(len(m_c)):
        t += m_c[i][j]

print(t//2)
