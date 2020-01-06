import sys
input = sys.stdin.readline

selected = [False]*50


def lotto(idx, cnt, s):
    if cnt == 6:
        tmp = []
        for i in range(len(s)):
            if selected[i]:
                tmp.append(s[i])
        print(' '.join(map(str, tmp)))
        return
    for i in range(idx, len(s)):
        if selected[i]:
            continue
        selected[i] = True
        lotto(i, cnt+1, s)
        selected[i] = False


while 1:
    ks = list(map(int, input().split()))
    if ks[0] == 0:
        break
    s = ks[1:]
    lotto(0, 0, s)
    print()
