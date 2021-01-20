n,m,*l=map(int,open(0).read().split())
d={}
for i,v in enumerate(sorted(l[:n])):d[v]=d.get(v,i)
print(*[d.get(i,-1) for i in l[n:]],sep='\n')