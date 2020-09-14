from collections import Counter


def solve():
    n, m = map(int, input().split())
    tree = sorted(Counter(map(int, input().split())).items(), reverse=True)
    l = 1
    r = tree[0][0]
    res = 0
    while l <= r:
        mid = (l+r) >> 1
        cnt = 0
        for t, v in tree:
            if t > mid:
                cnt += v*(t-mid)
            else:
                break
        if cnt >= m:
            l = mid+1
            res = max(res, mid)
        else:
            r = mid-1
    print(res)


if __name__ == '__main__':
    solve()
