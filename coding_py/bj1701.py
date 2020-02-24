P = input().rstrip()


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


res = 0
for i in range(len(P)):
    res = max(max(getPi(P[i:])), res)

print(res)
