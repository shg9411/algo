import re
p = re.compile('(100+1+|01)+$')
print("NOISE" if p.match(input().rstrip()) == None else "SUBMARINE")
