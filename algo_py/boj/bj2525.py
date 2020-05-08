a, b = map(int, input().split())
c = int(input())
x, y = divmod(c, 60)
b += y
if b >= 60:
    b -= 60
    a += 1
a += x
a %= 24
print(a, b)
