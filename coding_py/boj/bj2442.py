n = int(input())

for i in range(n):
    tmp = '*'*(i*2+1)
    print(tmp.center(2*n-1).rstrip())
