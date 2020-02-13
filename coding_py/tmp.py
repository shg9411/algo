n=int(input())
arr=list(map(int,input().split()))

d=[(0,0)]*n

for i in range(n):
    d[i]=(1,arr[i])
    for j in range(i):
        if (arr[i]>arr[j]) and (d[i][0]<d[j][0]+1):
            d[i]=(d[j][0]+1, arr[i])


d=list(set(d))
d.sort()

save=[]
save.append(d[0][1])

for i in range(1,len(d)):
    if d[i][0]==d[i-1][0]:
        continue
    save.append(d[i][1])
print(len(save))
for i in range(len(save)):
    print(save[i],end=' ')
