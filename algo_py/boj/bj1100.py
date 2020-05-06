chess = [None]*8
for i in range(8):
    chess[i] = list(input())
count = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and chess[i][j] == 'F':
            count += 1

print(count)
