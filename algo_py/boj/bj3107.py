res = input().split(':')
cnt = 0
x = -1
for i in range(len(res)):
    if not res[i]:
        res[i] = '0000'
        cnt += 1
        if cnt == 1:
            x = i
    else:
        tmp = res[i]
        diff = 4-len(tmp)
        res[i] = '0'*diff+tmp
if x == 7:
    res.pop()
if x == 0:
    res.pop(0)
for _ in range(8-len(res)):
    res.insert(x, '0000')
print(':'.join(res))