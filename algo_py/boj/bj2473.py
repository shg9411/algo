n = int(input())
val = sorted(list(map(int, input().split())))
res = 3*10**9+1
ans = (-1, -1, -1)

for i in range(n-2):
    j = i+1
    k = n-1
    while True:
        if j >= k:
            break
        x = val[i]+val[j]+val[k]
        nx = abs(x)
        if res > nx:
            res = nx
            ans = (val[i], val[j], val[k])
        if x > 0:
            k -= 1
        else:
            j += 1
print(*ans)
