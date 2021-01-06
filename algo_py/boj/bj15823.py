from collections import defaultdict

n, m = map(int, input().split())
card = list(map(int, input().split()))
l, r = 1, n+1
while l+1 < r:
    mid = (l+r) >> 1
    tmp = 0
    cnt = defaultdict(int)
    vcnt = 0
    i = j = 0
    while i < n:
        if cnt[card[i]] > 0:
            vcnt += 1
        cnt[card[i]] += 1
        if j == mid:
            cnt[card[i-mid]] -= 1
            if cnt[card[i-mid]] > 0:
                vcnt -= 1
        else:
            j += 1
        if j == mid and vcnt == 0:
            tmp += 1
            if tmp == m:
                break
            while j > 0:
                j -= 1
                cnt[card[i-j]] -= 1
        i += 1
    if tmp >= m:
        l = mid
    else:
        r = mid
print(l)
