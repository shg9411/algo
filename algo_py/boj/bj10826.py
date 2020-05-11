fibo = [0, 1]
n = int(input())

if n < 2:
    print(fibo[n])
else:
    for _ in range(n-1):
        fibo.append(fibo[-1]+fibo[-2])
    print(fibo[n])
