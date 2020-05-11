S = input()
T = input()
find = False
while 1:
    if len(S) == len(T):
        if S == T:
            find = True
        break
    tmp = T[-1]
    T = T[:-1]
    if tmp == 'B':
        T = T[::-1]
print(1 if find else 0)
