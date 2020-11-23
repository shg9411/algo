for _ in range(int(input())):
    y = k = 0
    for _ in range(9):
        y, k = map(sum(zip(map(int, input().split()), [y, k])))
    print(y, k)
