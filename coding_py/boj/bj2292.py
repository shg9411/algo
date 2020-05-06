n = int(input())

if n == 1:
    print(1)
else:
    n -= 1
    count = 1
    base = 6
    while 1:
        count += 1
        n -= base
        if n <= 0:
            print(count)
            break
        base += 6
