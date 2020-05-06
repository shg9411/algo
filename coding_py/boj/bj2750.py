N = int(input())
Nlist = []

for i in range(N):
    a = int(input())
    Nlist.append(a)

Nlist.sort()
print(Nlist)
print(set(Nlist))


for i in range(len(Nlist)):
    print(Nlist[i])
