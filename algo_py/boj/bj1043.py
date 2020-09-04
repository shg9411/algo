def main():
    _, m = map(int, input().split())
    _, *p = map(int, input().split())
    p = set(p)
    tmp = []
    ok = []
    for _ in range(m):
        tmp.append(set(map(int, input().split()[1:])))
        ok.append(1)

    for _ in range(m):
        for idx, party in enumerate(tmp):
            if p & party:
                ok[idx] = 0
                p |= party
    print(sum(ok))


if __name__ == '__main__':
    main()