x = [list(map(str, input())) for i in range(5)]
xx = []
for i in range(15):
    for j in range(5):
        if len(x[j]) <= i:
            continue
        else:
            xx.append(x[j][i])

print(''.join(xx))
