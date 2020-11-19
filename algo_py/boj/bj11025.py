n,m=map(int,input().split())
r=0
for i in range(1,n+1):
    r = (r+m)%i
print(r+1)