n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i])
    for j in range(i):
        if a[i] > a[j]:
            b[i] = max(a[i] + b[j], b[i])
print(max(b))