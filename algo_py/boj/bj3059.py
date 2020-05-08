t = int(input())
for _ in range(t):
    res = 2015
    tmp = set()
    for char in input().rstrip():
        if char in tmp:
            continue
        tmp.add(char)
        res -= ord(char)
    print(res)
