import sys
input = sys.stdin.readline


def solve():
    s, e = [], []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        s.append(x)
        e.append(y)
    s.sort()
    e.sort()
    i = j = cnt = 0
    res = 1
    while i < n:
        if s[i] < e[j]:
            i += 1
            cnt += 1
            res = max(res, cnt)
        else:
            j += 1
            cnt -= 1
    print(res)


if __name__ == '__main__':
    solve()
