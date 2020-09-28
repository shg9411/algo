import sys
i=lambda:map(int,sys.stdin.readline().split())
def f(x):
    if p[x]!=x:
        p[x]=f(p[x])
    return p[x]
    
while 1:
    m,n=i()
    if m==0and n==0:
        break
    p=list(range(m))
    q=[]
    t=0
    for _ in range(n):
        x,y,z=i()
        q+=(z,x,y),
        t+=z
    q.sort()
    r=ct=0
    for c,a,b in q:
        if f(a)==f(b):
            continue
        r+=c
        ct+=1
        p[f(b)] = f(a)
        if ct==m-1:
            print(t-r)