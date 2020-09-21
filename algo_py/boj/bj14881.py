import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("NO" if (c > a and c > b) or c % math.gcd(a, b) else "YES")
