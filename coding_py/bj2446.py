n = int(input())
arr = []
for i in range(n):
    arr.append(' '*i+'*'*((n-i-1)*2+1))
arr += arr[-2::-1]
print('\n'.join(arr))