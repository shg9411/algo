a, b = map(int, input().split())
L = []
n = 0
for x in range(1,a + b):
    n += x
    if n > a + b:
        break
    L.append(n)
print(L)
S = 0
for y in range(a,b+1):    
    for x in L:
        if y <= x:
            S += L.index(x) + 1
            break
print(S)

'''
test bat file  commit
'''
