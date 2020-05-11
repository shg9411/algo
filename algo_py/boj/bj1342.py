S = list(input())
alpha = [0 for _ in range(26)]
for char in S:
    alpha[ord(char)-ord('a')] += 1

res = 0


def dfs(pre, idx):
    global res
    if idx == length:
        res += 1
        return
    for i in range(26):
        if not alpha[i] or pre == i:
            continue
        alpha[i] -= 1
        dfs(i, idx+1)
        alpha[i] += 1


many = len(set(S))
length = len(S)
if many == 10:
    print(3628800)
elif many == 9 and length == 10:
    print(1451520)
elif many == 9 and length == 9:
    print(362880)
else:
    dfs(-1, 0)
    print(res)
