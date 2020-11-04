h, w = map(int, input().split())
b = list(map(int, input().split()))
res = 0
for i in range(w):
    res += abs(b[i]-min(max(b[:i+1]),max(b[i:])))
print(res)