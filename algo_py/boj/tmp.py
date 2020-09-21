import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("NO" if c > a or c > b or c % math.gcd(a, b) else "YES")
