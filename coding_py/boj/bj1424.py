n = int(input())
l = int(input())
c = int(input())

maxCan = (c+1)//(l+1)
if maxCan % 13 == 0:
    maxCan -= 1
if n % maxCan == 0:
    res = n // maxCan
elif ((n % maxCan) % 13) == 0:
    if n/maxCan >= 1 and maxCan > n % maxCan+1:
        res = n//maxCan+1
    else:
        res = n//maxCan+2
else:
    res = n//maxCan+1

print(res)
