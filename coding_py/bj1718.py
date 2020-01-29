real = input().rstrip()
key = input().rstrip()
keynum = []
for k in key:
    keynum.append(ord(k)-96)

res = []
kl = len(key)
for idx,r in enumerate(real):
    tmp = ord(r)
    idx %= kl
    if 97<=tmp<=122:
        char = tmp-keynum[idx]
        if char<97:
            char+=26
        res.append(chr(char))
    else:
        res.append(r)

print(''.join(res))
#97 - 122