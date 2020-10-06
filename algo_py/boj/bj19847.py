n=int(input());x,*f=map(int,input().split());c=x;p=[1]*c
for n in f:
    if n<c:
        for i in range(n,c):
            p[i%n]+=p[i]
        c=n
print(sum([i*v/x for i,v in enumerate(p[:c])]))
