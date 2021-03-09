n = int(input())

s = []
for i in range(2, int(n**0.5)+1):
    while not n % i:
        s.append(i)
        n //= i
if n != 1:
    s.append(n)

l = len(s)
if l == 1:
    print(-1)
else:
    res = []
    if l % 2:
        i = 0
        while i < l-3:
            res.append(s[i]*s[i+1])
            i += 2
        res.append(s[i]*s[i+1]*s[i+2])
    else:
        i = 0
        while i < l:
            res.append(s[i]*s[i+1])
            i += 2
    print(*res)
