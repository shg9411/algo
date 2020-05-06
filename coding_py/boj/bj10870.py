def fibo(i):
    if i==0:
        return 0
    if i <= 2:
        return 1
    return fibo(i-1) + fibo(i-2)


print(fibo(int(input())))
