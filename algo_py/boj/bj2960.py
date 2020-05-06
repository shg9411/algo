n, k = map(int, input().split())
x = [True for i in range(n+1)]
x[0] = x[1] = False
count = 0

while count < k:
    idx = x.index(True)
    for t in range(idx, n+1, idx):
        if x[t] == True:
            x[t] = False
            count += 1
            if count == k:
                print(t)
                break
