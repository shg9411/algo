t = int(input())
for _ in range(t):
    input()
    num = list(map(int, input().split()))
    tmp = res = num[0]
    for n in num[1:]:
        tmp = max(tmp+n, n)
        res = max(res, tmp)
    print(res)
