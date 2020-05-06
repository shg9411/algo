N = int(input())
S = list(map(int, input().split()))
numSet = set()


def dfs(i, val):
    if i == N:
        return

    dfs(i+1, val)
    dfs(i+1, val+S[i])
    numSet.add(val+S[i])


dfs(0, 0)

numList = sorted(list(numSet))

num = 0
while num < len(numList):
    if numList[num] != num+1:
        break
    num += 1
print(num+1)
