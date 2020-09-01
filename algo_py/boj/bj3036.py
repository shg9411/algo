import math
int(input())
num = list(map(int, input().split()))
for n in num[1:]:
    x = math.gcd(num[0], n)
    print(num[0]//x, n//x, sep='/')
