a,b = map(int,input().split())
tmp = [0]
for i in range(1,50):
    for j in range(i):
        tmp.append(i)

print(sum(tmp[a:b+1]))