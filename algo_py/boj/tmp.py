a,b = map(int,input().split())
if a>b:
    a,b = b,a
print(b-a-1)
print(' '.join(map(str,[i for i in range(a+1,b)])))