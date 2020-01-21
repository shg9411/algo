from decimal import getcontext, Decimal
getcontext().prec = 2000
a,b = map(Decimal,input().split())
print(a/b)