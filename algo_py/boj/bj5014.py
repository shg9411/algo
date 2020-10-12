f,s,g,u,d=map(int,input().split())
r=0
while r<f and 0<s and s<= f:
    if s==g:
        print(r)
        exit()
    s-=d if s>g and s>d or s<g and s+u>f else-u
    r+=1
print("use the stairs")