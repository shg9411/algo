import sys
input = sys.stdin.readline

selected = [False]*50


def lotto(idx, cnt, s):
    if idx == len(s):
        return
    if cnt == 6:
        tmp = []
        for i in range(len(s)):
            if selected[i]:
                tmp.append(s[i])
        print(' '.join(map(str, tmp)))
        return
    selected[idx] = True
    lotto(idx, cnt+1, s)
    selected[idx] = False
    lotto(idx+1, cnt, s)


while 1:
    ks = list(map(int, input().split()))
    if ks[0] == 0:
        break
    s = ks[1:]
    lotto(0, 0, s)
    print()
