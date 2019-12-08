n, m = map(int, input().split())
one = []
six = []
v = 1001
for _ in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)
o = min(one)
s = min(six)
price = 0
if o*6 <= s:
    price = o*n
else:
    price = s * (n//6)
    if n % 6 != 0:
        if o * (n % 6) > s:
            price += s
        else:
            price += o * (n % 6)

print(price)
