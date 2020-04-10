import sys
n = int(input())
num = sorted(list(map(int, input().split())))
i = 0
j = n-1
x = num[i]
y = num[j]
diff = abs(num[j]+num[i])
while i < j:
    tmp = num[i]+num[j]
    if diff > abs(tmp):
        diff = abs(tmp)
        x = num[i]
        y = num[j]
    if tmp > 0:
        j -= 1
    else:
        i += 1
print(x, y)
