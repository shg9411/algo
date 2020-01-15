n = int(input())
many = list(map(int, input().split()))

res = []

for i in range(n-1, -1, -1):
    res.insert(many[i],i+1)

print(' '.join(map(str,res)))