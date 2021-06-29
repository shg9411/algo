n = int(input())
tf = [[0]*26 for _ in range(26)]
for _ in range(n):
    a, b = map(lambda x: ord(x)-97, input().split(' is '))
    tf[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if tf[i][k] and tf[k][j]:
                tf[i][j] = 1

for _ in range(int(input())):
    a, b = map(lambda x: ord(x)-97, input().split(' is '))
    print('T' if tf[a][b] else 'F')