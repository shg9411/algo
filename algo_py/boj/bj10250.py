import sys
import math
input = sys.stdin.readline

t = int(input())

while t:
    t -= 1
    h, w, n = map(int, input().split())
    print('%d%02d' % (n % h, math.ceil(n/h)) if n %
          h != 0 else '%d%02d' % (h, math.ceil(n/h)))
