l = []
notFill = []
numset = set(range(1, 10))
for i in range(9):
    l.append(list(map(int, input().split())))
    for j in range(9):
        if l[i][j] == 0:
            notFill.append((i, j))


def f(idx):
    if idx == len(notFill):
        for line in l:
            print(' '.join(map(str, line)))
        exit()
    i, j = notFill[idx]

    I = i//3*3
    J = j//3*3
    for n in numset.difference(set(l[i] + [l[i][j] for i in range(9)] + l[I][J:J+3]+l[I+1][J:J+3]+l[I+2][J:J+3])):
        l[i][j] = n
        f(idx+1)
        l[i][j] = 0


f(0)
