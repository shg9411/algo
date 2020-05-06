n, b = input().split()

res = 0
cur = 1
for i in range(len(n)-1, -1, -1):
    if n[i].isalpha():
        res += cur * (ord(n[i])-55)
    else:
        res += cur * int(n[i])
    cur *= int(b)
print(res)
