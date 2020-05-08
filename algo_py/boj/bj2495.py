for _ in range(3):
    s = input().rstrip()+' '
    res = 0
    cnt = 1
    for i in range(8):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 1
    print(res)
