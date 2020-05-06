import math
a,b,c,d = map(int,input().split())
 
if math.ceil(c/b) <= math.ceil(a/d):
  print("YES")
else:
  print("NO")