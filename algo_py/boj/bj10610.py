n = list(map(int,list(input())))

if sum(n)%3!=0 or 0 not in n:
    print(-1)
    exit()

n.sort(reverse=True)

print(''.join(map(str,n)))