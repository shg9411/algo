import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
time = [(0, 0)]
for _ in range(n):
    time.append(tuple(map(int, input().split())))
time.sort()

for i in range(n):
    if time[i+1][0]-(et := time[i][0]+time[i][1]) >= m:
        print(et)
        exit()
i += 1
if time[i][0]+time[i][1]+m <= s:
    print(time[i][0]+time[i][1])
else:
    print(-1)
