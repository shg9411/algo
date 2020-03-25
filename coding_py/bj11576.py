a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))[::-1]
res = 0
for i in range(m):
    res += num[i]*(a**i)
tmp = []

while res>0:
    tmp.append(res%b)
    res = res//b
print(' '.join(map(str,tmp[::-1])))