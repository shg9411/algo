a, b = map(int, input().split())
for i in range(a, b+1):
    chk = True
    for j in range(2, int(i**0.5)+1):
        print(i,j)
        if i % j == 0:
            chk = False
            break
    if chk and i != 1:
        #print(i)
        pass
