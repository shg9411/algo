def getPrime(n):
    s = [0, 0]+[1 for _ in range(n-1)]
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i):
                s[j] = 0
    return s
