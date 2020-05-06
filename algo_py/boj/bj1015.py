input()
a = list(map(int, input().split()))
b = [i for i in range(len(a))]

for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            tmpa,tmpb = a[j],b[j]
            a[j],b[j] = a[j+1],b[j+1]
            a[j+1],b[j+1] = tmpa,tmpb
s = [0]*len(a)
for i in range(len(a)):
    s[b[i]] = i
print(' '.join(map(str,s)))