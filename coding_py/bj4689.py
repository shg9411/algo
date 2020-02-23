import sys
numList = '0123456789ABCDEF'
for line in sys.stdin:
    num1, num2, num3 = line.split()
    num2, num3 = int(num2), int(num3)
    total = 0
    i = 0
    for c in num1[::-1]:
        total += numList.index(c)*(int(num2)**i)
        i += 1
    tmp = ''
    while total != 0:
        total, div = divmod(total, num3)
        tmp += numList[div]
    if len(tmp) > 7:
        print("%7s" % "ERROR")
    else:
        print("%7s" % tmp[::-1])
