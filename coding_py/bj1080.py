n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]
answer = 0
if n < 3 or m < 3:
    pass
else:
    for i in range(n):
        for j in range(m):
            if a[i][j] == b[i][j]:
                continue
            for k in range(3):
                for h in range(3):
                    if a[i+k][j+h] == '1':
                        a[i+k][j+h] = '0'
                    else:
                        a[i+k][j+h] = '1'
            answer += 1
if a == b:
    print(answer)
else:
    print(-1)
