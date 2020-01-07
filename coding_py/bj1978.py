n = int(input())
num = list(map(int, input().split()))
sosu = [True] * (max(num)+1)
sosu[1] = False
for i in range(2, int(len(sosu)**0.5)+1):
    if sosu[i]:
        for j in range(i+i, max(num)+1, i):
            sosu[j] = False
count = 0
for n in num:
    if sosu[n]:
        count+=1

print(count)