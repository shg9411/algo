val = 0
x, y = -1, -1
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] > val:
            val = tmp[j]
            x, y = i+1, j+1
print(val)
print(x, y)
