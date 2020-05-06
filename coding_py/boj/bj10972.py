import sys
input = sys.stdin.readline

n = int(input())

string = list(map(int, input().split()))

find = False
for i in range(n-1, 0, -1):
    if string[i-1] < string[i]:
        find = True
        break
if not find:
    print(-1)
    exit()
else:
    for j in range(n-1,i-1,-1):
        if string[i-1]<string[j]:
            string[i-1],string[j] = string[j],string[i-1]
            break

    while i < n-1:
        string[i],string[n-1] = string[n-1],string[i]
        i+=1
        n-=1

print(' '.join(map(str, string)))