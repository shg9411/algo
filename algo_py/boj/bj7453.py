import sys
input = sys.stdin.readline
x = 1 << 8


def solve():
    n = int(input())
    num = list(zip(*[list(map(int, input().split())) for _ in range(n)]))
    radix = [[[] for _ in range(x)] for _ in range(4)]
    vst = [0]*2097153
    cnt = [0]*2097153

    for i in range(n):
        for j in range(n):
            tmp = num[0][i]+num[1][j]
            if tmp > 0:
                radix[0][tmp & 255].append(tmp >> 8)
            else:
                tmp = -tmp
                radix[1][tmp & 255].append(tmp >> 8)
            tmp = num[2][i]+num[3][j]
            if tmp >= 0:
                radix[2][tmp & 255].append(tmp >> 8)
            else:
                tmp = -tmp
                radix[3][tmp & 255].append(tmp >> 8)

    vstCnt = 1
    ans = 0
    for i in range(x):
        vstCnt += 1
        for n in radix[0][i]:
            if vst[n] < vstCnt:
                vst[n] = vstCnt
                cnt[n] = 1
            else:
                cnt[n] += 1
        for n in radix[3][i]:
            if vst[n] == vstCnt:
                ans += cnt[n]
        vstCnt += 1
        for n in radix[1][i]:
            if vst[n] < vstCnt:
                vst[n] = vstCnt
                cnt[n] = 1
            else:
                cnt[n] += 1
        for n in radix[2][i]:
            if vst[n] == vstCnt:
                ans += cnt[n]
    print(ans)


if __name__ == '__main__':
    solve()
