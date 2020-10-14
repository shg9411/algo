n = int(input())
numDict = {i: 0 for i in 'ABCDEFGHIJ'}
not_to_zero = set()
for _ in range(n):
    num = input()
    numLen = len(num)
    v = 0
    for i in range(numLen-1, -1, -1):
        if i == 0:
            not_to_zero.add(num[i])
        numDict[num[i]] += 10**v
        v += 1
num = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
print(num)
if num[-1][1] != 0:
    for i in range(9, -1, -1):
        if num[i][0] not in not_to_zero:
            tmp = list(num[i])
            num.append(num.pop(i))
            break

ans = 0
for i in range(10):
    ans += num[i][1]*(9-i)
print(ans)
