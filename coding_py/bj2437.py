n = int(input())
chu = list(map(int, input().split()))
chu.sort()
minV = 1
for s in range(n):
    if chu[s] <= minV:
        minV += chu[s]
    else:
        break
print(minV)
