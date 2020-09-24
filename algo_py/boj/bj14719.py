def solve():
    h, w = map(int, input().split())
    b = list(map(int, input().split()))

    def r(b):
        x = 0
        for i in range(len(b)):
            ml = max(b[:i+1])
            mr = max(b[i:])
            ll = min(ml, mr)
            x = x + abs(b[i] - ll)
        return x

    print(r(b))


if __name__ == '__main__':
    solve()
