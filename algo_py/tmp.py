import sys
n = int(input())
lst = []
result = []
for _ in range(n):
    lst.append(list(sys.stdin.readline().strip()))

def div_con(x, y, n):
    s=[]
    global result
    for i in range(x, x+n):
        for j in range(y, y+n):
            s.append(lst[i][j])

    if s == ['0' for i in range(n*n)]:
        result.append(0)
    elif s == ['1' for i in range(n*n)]:
        result.append(1)
    else:
        result.append("(")
        div_con(x, y, n//2)
        div_con(x, y + n//2, n//2)
        div_con(x + n//2, y, n//2)
        div_con(x + n//2, y + n//2, n//2)
        result.append(")")

    return result

result = div_con(0, 0, n)
for i in result:
    print(i, end='')