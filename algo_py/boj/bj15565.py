
def solve():
    n, k = map(int, input().split())
    doll = list(input().split())
    i = j = 0
    res = n+1
    cnt = 0

    while 1:
        if cnt == k:
            res = min(j-i, res)
            if doll[i] == '1':
                cnt -= 1
            i += 1
        elif j == n:
            break
        else:
            if doll[j] == '1':
                cnt += 1
            j += 1
    print(res if res < n+1 else -1)


if __name__ == '__main__':
    solve()
