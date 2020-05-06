n = int(input())
tmp1,tmp2 = 0,1
for i in range(2,n+1):
    tmp1,tmp2 = tmp2,(tmp1+tmp2)%1000000007
print(tmp2 if n>=2 else n)