a, b = map(int, input().split())
if a<b:
    b,a=a,b
while b:
    r = a%b
    a = b
    b = r

print(a*'1')
