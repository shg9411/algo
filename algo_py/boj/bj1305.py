import sys
input = sys.stdin.readline


def getPi(pattern):
    strlen = len(pattern)
    j = 0
    pi = [0 for _ in range(strlen)]
    for i in range(1, strlen):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


while 1:
    tmp = input().rstrip()
    if tmp == '.':
        break
    res = getPi(tmp)
    print(res)
    print(len(tmp)//res.index(1) if 1 in res else 1)
