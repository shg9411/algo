n = int(input())

for i in range(max(1,n-9*len(str(n))), n):
    if i+sum(list(map(int, str(i)))) == n:
        print(i)
        exit()
print(0)
