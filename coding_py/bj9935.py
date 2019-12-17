import sys
target = input()
tl = len(target)
bomb = input()
bl = len(bomb)

check = []
cl = 0
i = 0
while i < tl:
    check.append(target[i])
    cl += 1
    i += 1
    if cl >= bl:
        delete = True
        for j in range(-1, -bl-1, -1):
            if check[j] != bomb[j]:
                delete = False
                break
        if delete:
            a = 0
            while a < bl:
                check.pop()
                cl -= 1
                a += 1

print(''.join(check) if cl else 'FRULA')
