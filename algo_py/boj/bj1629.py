A, B, C = map(int, input().split())

ans = 1
mul = A % C
while B > 0:
    if B % 2 == 1:
        ans *= mul
        ans %= C
    mul = (mul % C)**2 % C
    B //= 2
print(ans)
