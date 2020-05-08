input()
res = 0
for a, b in zip(sorted(list(map(int, input().split())), reverse=True), sorted(list(map(int, input().split())))):
    res += a*b
print(res)
