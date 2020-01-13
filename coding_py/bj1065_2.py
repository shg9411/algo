n = int(input())
if n==1000:
    n-=1
res = 0
for i in range(1, n+1):
    if i <= 99:
        res += 1
    else:
        a, b, c = map(int, str(i))
        if a-b == b-c:
            res += 1
            print(i)
print(res)
