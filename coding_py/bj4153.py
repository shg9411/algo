while 1:
    z = list(map(int, input().split()))
    if z[0] == 0 and z[1] == 0 and z[2] == 0:
        break
    z.sort()
    if z[0]**2 + z[1] ** 2 == z[2]**2:
        print("right")
    else:
        print("wrong")
