n, m, k = map(int, input().split())
total = n+m
can = 0
for i in range(1, m+1):
    tmp = 3*i
    if 3*i+k <= total and i*2 <= n:
        can += 1
print(can)
