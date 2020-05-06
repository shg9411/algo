nan = sorted([int(input()) for _ in range(9)])
total = sum(nan)
for i in range(8):
    for j in range(i, 9):
        if total-nan[i]-nan[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(nan[k])
            exit()
