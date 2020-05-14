n = int(input())
prefix = list(input().rstrip())
alpha = [int(input()) for _ in range(n)]
res = []
for char in prefix:
    if char.isalpha():
        res.append(alpha[ord(char)-ord('A')])
    else:
        tmp1 = str(res.pop())
        tmp2 = str(res.pop())
        res.append(eval(tmp2+char+tmp1))
print('%.2f' % res[0])