n = int(input())
a = [" "]*n

for i in range(0, n):
    a[i] = input()
max = 0
for i in range(0, n):
    if len(a[i]) > max:
        max = len(a[i])
b = [0]*max
for i in range(1, n):
    for j in range(0, max):
        if b[j] != 2:
            if a[i][j] == a[i-1][j]:
                b[j] = 1
            else:
                b[j] = 2
for i in range(0, max):
    if b[i] == 1:
        print(a[0][i], end="")
    else:
        print("?", end="")
