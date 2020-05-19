n = int(input())
num = list(map(int, input().split()))

sums = [num[0]]
for i in range(1, n):
    sums.append(sums[-1]+num[i])
res = 0

for i in range(n):
    res += (sums[n-1]-sums[i])*num[i]
print(res)
