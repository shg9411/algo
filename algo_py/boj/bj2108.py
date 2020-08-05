import sys
input = sys.stdin.readline

n = int(input())

num = []
numDict = dict()

for _ in range(n):
    tmp = int(input())
    num.append(tmp)
    try:
        numDict[tmp] += 1
    except:
        numDict[tmp] = 1

num.sort()
sortedDict = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
manyNum = [sortedDict[0][0]]
temp = sortedDict[0][1]
for i in range(1, len(sortedDict)):
    if sortedDict[i][1] == temp:
        manyNum.append(sortedDict[i][0])
    else:
        break
print(round(sum(num)/n))
print(num[n//2])
print(sorted(manyNum)[1] if len(manyNum) > 1 else manyNum[0])
print(max(num)-min(num))