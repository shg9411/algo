a, b, c = map(int, input().split())
x = (a+b-c)/2
y = (a+c-b)/2
z = (b+c-a)/2
if x <= 0 or y <= 0 or z <= 0:
    print(-1)
    exit()
print(1)
print(x, y, z)
