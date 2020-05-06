n = int(input())
que = sorted(list(map(int, input().split())))
sum = 0
real = 0
for i in range(n):
    sum += que[i]
    real += sum

print(real)
