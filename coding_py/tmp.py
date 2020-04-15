for i in range(100):
    n = i
    cycle = 1
    if n < 10:
        n = int("0"+str(n))
    a = n//10
    b = n % 10
    c = b*10+(a+b) % 10
    while True:
        cycle = cycle+1
        if c < 10:
            c = int("0"+str(c))
        d = c//10
        e = c % 10
        f = e*10+(d+e) % 10
        if f == n:
            print(cycle)
            break
        else:
            c = f
