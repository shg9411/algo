n = int(input())
pt = [input() for _ in range(n)]

result = ''
for i in range(len(pt[0])):
    col = [x[i] for x in pt]
    if col.count(pt[0][i]) != n:
        result += '?'
    else:
        result += pt[0][i]
print(result)
