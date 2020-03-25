import sys
n = int(input())
tmp = list(map(int, input().split()))
test = sys.stdin.read()
if test:
    tmp += list(map(int, test.split()))
# print(tmp)


num = tmp[:]
res = []
check = 0
for i in range(n):
    if num[i] != i+1:
        idx = num.index(i+1)
        if i == 0:
            num = num[:i] + num[idx::-1] + num[idx+1:]
        else:
            num = num[:i] + num[idx:i-1:-1] + num[idx+1:]
        check += 1
        res.append([i+1, idx+1])
        break
if check == 0:
    print(1, 1)
    print(1, 1)
    exit()
for i in range(n):
    if num[i] != i+1:
        idx = num.index(i+1)
        if i == 0:
            num = num[:i] + num[idx::-1] + num[idx+1:]
        else:
            num = num[:i] + num[idx:i-1:-1] + num[idx+1:]
        check += 1
        res.append([i+1, idx+1])
        break

if num == sorted(tmp):
    for t in res:
        print(' '.join(map(str, t)))
    if check == 1:
        print(1, 1)
    exit()
# print(num)
num = tmp[:]
check = 0
res = []
for i in range(n-1, -1, -1):
    if num[i] != i+1:
        idx = num.index(i+1)
        if idx == 0:
            num = num[i::-1]+num[i+1:]
        else:
            num = num[:idx] + num[i:idx-1:-1] + num[i+1:]
        check += 1
        res.append([idx+1, i+1])
        break
if num == sorted(tmp):
    for t in res:
        print(' '.join(map(str, t)))
    if check == 1:
        print(1, 1)
    exit()
for i in range(n-1, -1, -1):
    if num[i] != i+1:
        idx = num.index(i+1)
        if idx == 0:
            num = num[i::-1]+num[i+1:]
        else:
            num = num[:idx] + num[i:idx-1:-1] + num[i+1:]
        check += 1
        res.append([idx+1, i+1])
        break
if num == sorted(tmp):
    for t in res:
        print(' '.join(map(str, t)))
