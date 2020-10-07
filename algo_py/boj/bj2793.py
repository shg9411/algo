def c(n, a, d):
    return 0 if n-a < 0 else 1+(n-a)//d


a = [3, 6, 420, 360360, 72201776446800]
d = [2]+[0]*4
strlen = [2]+[0]*4
for i in range(1, 5):
    d[i] = 2*a[i]
    strlen[i] = 4
A, B = map(int, input().split())
res = 0
r = B-A+1
for i in range(5):
    tres = c(B, a[i], d[i])-c(A-1, a[i], d[i])
    res += (strlen[i]*tres)
    r -= tres
print(res+r*3)