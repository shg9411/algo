n, b = map(int, input().split())
res = ''

while n :
    div = n % b
    if div > 9:
        res += (chr(div+55))
    else:
        res += str(div)
    n = n // b
print(res[::-1])
