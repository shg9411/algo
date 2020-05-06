n = int(input())
numDict = {i: 0 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for _ in range(n):
    tmp = input().rstrip()
    x = 1
    for i in range(len(tmp)-1, -1, -1):
        numDict[tmp[i]] += x
        x *= 10

res = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
ans = 0
idx = 0
while res[idx][1] != 0:
    ans += res[idx][1] * (9-idx)
    idx += 1
print(ans)
