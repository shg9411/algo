n=int(input())
a=[0]
p=[[0,0]]
for i in range(1,n+1):
    a.append(int(input()))
p.append([a[1],0])
p.append([a[1]+a[2],a[2]])

for i in range(3,n+1):
    p.append([a[i]+p[i-1][1],max(a[i]+p[i-2][0],a[i]+p[i-2][1])])

print(max(p[n]))
