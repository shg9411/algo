n = int(input())
ar = list(map(int, input().split()))
s = []
for i in range(n-1, -1, -1):
    s.insert(ar[i], i+1)
for tmp in s:
    print(tmp, end = ' ')
