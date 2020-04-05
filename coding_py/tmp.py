N = int(input())
print(N)
res = [1, 2]
for i in range(1, N-2):
    res.append(i+2)
res.append(997)
print(*res)
