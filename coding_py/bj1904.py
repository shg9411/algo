N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    tmp1 = 1
    tmp2 = 2
    tmp = 0
    for i in range(2, N):
        tmp = (tmp1 + tmp2)%15746
        tmp1, tmp2 = tmp2, tmp
    print(tmp % 15746)
