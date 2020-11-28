res = 0


def check(mid):
    cnt = 0
    here = -1
    for p in w:
        if here <= p:
            cnt += 1
            here = p+mid
    return cnt >= m


def bs(s, e):
    global res
    for i in range(100):
        mid = (s+e) >> 1
        if check(mid):
            s = mid+1
            res = max(res, mid)
        else:
            e = mid-1


n, m, k = map(int, input().split())
w = list(map(int, input().split()))
bs(0, w[-1])
r = ''
cnt = 0
here = -1
for p in w:
    if here <= p and cnt < m:
        r += '1'
        here = p+res
        cnt += 1
    else:
        r += '0'
print(r)
