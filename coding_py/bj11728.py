n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = []
i,j = 0,0
al = len(a)
bl = len(b)
while i<al and j <bl:
    if a[i] > b[j]:
        res.append(b[j])
        j+=1
    else:
        res.append(a[i])
        i+=1

if i <= al-1:
    res.extend(a[i:al])
if j <= bl-1:
    res.extend(b[j:bl])
print(' '.join(str(n) for n in res))

