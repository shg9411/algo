n = int(input())
white = [[False]*100 for i in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if not white[i][j]:
                white[i][j] = True
count = 0
for x in range(100):
    count += white[x].count(True)

print(count)
