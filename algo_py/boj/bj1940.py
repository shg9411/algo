n = int(input())
m = int(input())
x = sorted(map(int, input().split()))
s = 0
e = n-1
cnt = 0
while s < e:
    if x[s]+x[e] < m:
        s += 1
    elif x[s]+x[e] > m:
        e -= 1
    else:
        cnt += 1
        s += 1
        e -= 1
print(cnt)
