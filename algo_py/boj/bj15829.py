n = int(input())
char = input().rstrip()
res = 0
cur = 1
mod = 1234567891
for i in range(n):
    res += (ord(char[i])-96)*cur
    res %= mod
    cur *= 31
    cur %= mod
print(res)