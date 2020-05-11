while 1:
    n, r = map(int, input().split())
    if n==0 and r == 0:
        break
    if n-r < r:
        r = n-r
    ans = div = 1
    while r:
        ans*=n
        ans//=div
        n-=1
        r-=1
        div+=1
    print(ans)
