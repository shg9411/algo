T = ''.join((c for c in input().rstrip() if c.isalpha()))
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


def kmp(text, pattern):
    pi = getPi(pattern)
    tLen = len(text)
    sLen = len(pattern)
    j = 0
    for i in range(tLen):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            if j == sLen-1:
                return 1
            j += 1
    return 0


print(kmp(T, P))
