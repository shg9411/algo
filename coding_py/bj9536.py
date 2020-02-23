import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sounds = sys.stdin.readline().split()
    notFox = dict()
    while 1:
        tmp = sys.stdin.readline().rstrip()
        if tmp == "what does the fox say?":
            break
        tmp = tmp.split()
        notFox[tmp[2]] = tmp[0]
    res = []
    for sound in sounds:
        if sound in notFox:
            continue
        res.append(sound)
    print(' '.join(res))
