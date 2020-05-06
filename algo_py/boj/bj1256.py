n, m, k = map(int, input().split())

make = [[0 for _ in range(101)] for _ in range(201)]
res = ''
make[0][0] = 1
for i in range(1, n+m+1):
    make[i][0] = 1
    for j in range(1, i):
        if j > m:
            break
        make[i][j] = min(make[i-1][j-1] + make[i-1][j], 1000000000)
    if i <= m:
        make[i][i] = 1
k -= 1
if make[n+m][m] <= k:
    print(-1)
    exit()
for i in range(n+m-1, -1, -1):
    if i >= m and make[i][m] > k:
        res += 'a'
    else:
        res += 'z'
        k -= make[i][m]
        m -= 1
print(res)
