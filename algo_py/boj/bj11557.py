for _ in range(int(input())):
    n = int(input())
    s = dict()
    for _ in range(n):
        a, b = input().split()
        s[a] = int(b)
    print(sorted(s.items(), key=lambda x: x[1])[-1][0])
