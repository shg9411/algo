n = int(input())
m = int(input())
s = input().rstrip()

text = 'I'+'OI'*n


def getPi(p):
    pl = len(p)
    kmp = [0 for _ in range(pl)]
    j = 0
    for i in range(1, pl):
        while j > 0 and p[i] != p[j]:
            j = kmp[j-1]
        if p[i] == p[j]:
            j += 1
            kmp[i] = j
    return kmp


def getAnswer(p,s):
    res = 0
    pi = getPi(p)
    #print(pi)
    sl = len(s)
    pl = len(p)
    j = 0
    for i in range(sl):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i]==p[j]:
            if j==pl-1:
                res+=1
                j = pi[j]
            else:
                j+=1
    return res


print(getAnswer(text,s))
