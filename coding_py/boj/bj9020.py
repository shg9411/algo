
sosu = [True for _ in range(10001)]
sosu[0] = sosu[1] = False

for i in range(2, 101):
    if sosu[i]:
        for j in range(i*2, 10001, i):
            sosu[j] = False

t = int(input())

for _ in range(t):
    num = int(input())
    for i in range(num//2, 10001):
        if sosu[i] and sosu[num-i]:
            print(num-i, i)
            break
