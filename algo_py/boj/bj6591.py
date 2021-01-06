import math
while 1:
    n,r=map(int,input().split())
    if n==0and r == 0:
        break
    print(math.comb(n,r))
