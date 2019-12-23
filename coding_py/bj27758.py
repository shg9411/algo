import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k, n = int(input()), int(input())
    if n == 1:
        print(1)
        continue
    people = [[0 for _ in range(n)] for _ in range(k+1)]
    people[0] = [i for i in range(1,n+1)]
    for i in range(1, k+1):
        for j in range(n):
            people[i][j] = people[i-1][j]+people[i][j-1]
    print(people[k][n-1])
