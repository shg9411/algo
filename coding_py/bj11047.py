n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
count = 0
for i in range(n):
    count += k//coin[i]
    k %= coin[i]
    if k==0:
        break
print(count)