import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

piece = 1001
package = 1001

for _ in range(m):
    x, y = map(int, input().split())
    package = min(x, package)
    piece = min(y, piece)

if piece*6 <= package:
    print(piece*n)
else:
    price = package*(n//6)
    price += min(piece*(n % 6), package)
    print(price)
